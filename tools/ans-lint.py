#!/usr/bin/env python3
"""ans-lint — Agent-Native Specification 一致性门禁（公理①②的自我实践）。

校验 ans.json（机器可读契约）与 SPEC.md / CHECKLIST.md / ASSESSMENT.md /
changelog.json / compatibility.json 派生物一致。结构不一致即 exit 1（语义化退出码），
报告为机器可读 JSON（stdout）+ 人读摘要（stderr）。

用法:
    python3 tools/ans-lint.py            # 校验本仓
    python3 tools/ans-lint.py --json     # 仅输出 JSON 报告
环境变量 ANS_DIR 可覆盖仓根（便于喂篡改副本做负向测试）。
"""
import json
import os
import re
import sys

ROOT = os.environ.get("ANS_DIR") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EXPECTED_LEVEL_REQUIRES = {
    "L0": [],
    "L1": ["axiom1"],
    "L2": ["axiom1", "axiom2", "axiom3"],
    "L3": ["axiom1", "axiom2", "axiom3", "axiom4"],
}

errors = []
warnings = []
checks = []


def check(name, ok, detail=""):
    checks.append({"name": name, "ok": bool(ok), "detail": detail})
    if not ok:
        errors.append(f"{name}: {detail}")


def read(path):
    with open(os.path.join(ROOT, path), encoding="utf-8") as f:
        return f.read()


def load_json(path):
    return json.loads(read(path))


# ---- 解析 ans.json ----
ans = load_json("ans.json")
ans_clauses = [c for ax in ans["axioms"] for c in ax["clauses"]]
ans_ids = [c["id"] for c in ans_clauses]
ans_level = {c["id"]: c["level"] for c in ans_clauses}
ans_text = {c["id"]: c["text"] for c in ans_clauses}
# 公理 -> 有序 text 列表（用于与 CHECKLIST 逐条比对）
ans_axiom_texts = {ax["id"]: [c["text"] for c in ax["clauses"]] for ax in ans["axioms"]}
ans_axiom_order = [ax["id"] for ax in ans["axioms"]]

# ---- 解析 ASSESSMENT.md：- [ ] `A1.1` [MUST] text ----
asmt = read("ASSESSMENT.md")
ASMT_RE = re.compile(r"^- \[[ x]\] `(A\d\.\d)` \[(MUST|SHOULD)\] (.+?)\s*$", re.M)
asmt_rows = ASMT_RE.findall(asmt)
asmt_ids = [r[0] for r in asmt_rows]
asmt_level = {r[0]: r[1] for r in asmt_rows}

# ---- 解析 CHECKLIST.md：四问块 + 各公理块的 - [ ] 行 ----
chk = read("CHECKLIST.md")
# 切块：## 标题
blocks = re.split(r"^## ", chk, flags=re.M)
chk_axiom_texts = {}   # axiom_id -> 有序 text 列表
chk_fourq = 0
ITEM_RE = re.compile(r"^- \[[ x]\] (.+?)\s*$", re.M)
AXIOM_NAME_TO_ID = {ax["name"]: ax["id"] for ax in ans["axioms"]}
for b in blocks:
    head = b.splitlines()[0] if b else ""
    items = ITEM_RE.findall(b)
    if head.startswith("四问速判"):
        chk_fourq = len(items)
    else:
        for name, aid in AXIOM_NAME_TO_ID.items():
            if name in head:
                # 去掉条目里可能的 markdown 加粗，仅取纯 text
                chk_axiom_texts[aid] = [re.sub(r"\*\*", "", t) for t in items]

# ---- 解析 SPEC.md 头部 version / stage ----
spec = read("SPEC.md")
m_ver = re.search(r"版本\s+(\d+\.\d+\.\d+)", spec)
m_stage = re.search(r"(Draft|Candidate|Stable)", spec)
spec_version = m_ver.group(1) if m_ver else None
spec_stage = m_stage.group(1) if m_stage else None

# ---- 解析 changelog / compatibility ----
changelog = load_json("changelog.json")
compat = load_json("compatibility.json")

# ================= 校验 =================

# 1. clause 数量
check("clause-count==19", len(ans_ids) == 19, f"ans.json 有 {len(ans_ids)} 条")

# 2. id 唯一
check("clause-id-unique", len(ans_ids) == len(set(ans_ids)), "ans.json clause id 有重复")

# 3. ans ids == assessment ids（集合）
miss_in_asmt = set(ans_ids) - set(asmt_ids)
extra_in_asmt = set(asmt_ids) - set(ans_ids)
check("ans==ASSESSMENT ids", not miss_in_asmt and not extra_in_asmt,
      f"ASSESSMENT 缺 {sorted(miss_in_asmt)}；多 {sorted(extra_in_asmt)}")

# 4. level 一致（ans vs assessment）
lvl_mismatch = [i for i in ans_ids if i in asmt_level and ans_level[i] != asmt_level[i]]
check("level ans==ASSESSMENT", not lvl_mismatch,
      "; ".join(f"{i}: ans={ans_level[i]} asmt={asmt_level[i]}" for i in lvl_mismatch))

# 5. ans vs CHECKLIST：每公理条数 + 逐条 text 一致
for aid in ans_axiom_order:
    a_texts = ans_axiom_texts[aid]
    c_texts = chk_axiom_texts.get(aid, [])
    if len(a_texts) != len(c_texts):
        check(f"{aid} count ans==CHECKLIST", False, f"ans={len(a_texts)} checklist={len(c_texts)}")
        continue
    check(f"{aid} count ans==CHECKLIST", True)
    drift = [(a, c) for a, c in zip(a_texts, c_texts) if a != c]
    check(f"{aid} text ans==CHECKLIST", not drift,
          "; ".join(f"[{a!r} != {c!r}]" for a, c in drift))

# 6. 四问数量一致
check("fourQuestions==4 (ans)", len(ans["fourQuestions"]) == 4, str(len(ans["fourQuestions"])))
check("fourQuestions==4 (CHECKLIST)", chk_fourq == 4, str(chk_fourq))

# 7. 成熟度级别定义
lvl_req = {l["id"]: l["requires"] for l in ans["levels"]}
check("levels match SPEC §3.2", lvl_req == EXPECTED_LEVEL_REQUIRES, f"got {lvl_req}")

# 8. 版本 / 阶段一致
check("version ans==SPEC", ans["version"] == spec_version, f"ans={ans['version']} spec={spec_version}")
check("stage ans==SPEC", ans["stage"] == spec_stage, f"ans={ans['stage']} spec={spec_stage}")
latest = changelog[0]
check("version ans==changelog", ans["version"] == latest["version"],
      f"ans={ans['version']} changelog={latest['version']}")

# 9. changelog 条目 id 均属 ans
bad_cl = [c["entryId"] for c in latest["changes"] if c.get("entryId") and c["entryId"] not in set(ans_ids)]
check("changelog entryIds ⊆ ans", not bad_cl, f"未知 id: {bad_cl}")

# 10. compatibility 字段齐全
compat_ok = all(
    all(k in row for k in ("fromVersion", "toVersion", "breaking", "removedEntryIds", "tightenedEntryIds"))
    for row in compat
)
check("compatibility schema", compat_ok, "缺字段")
check("compatibility covers current", any(r["toVersion"] == ans["version"] for r in compat),
      f"无 toVersion={ans['version']} 记录")

# 11. SPEC 正文 normative 条目结构与 ans.json 对齐（防 SPEC-only 漂移）
#     SPEC 是真源，但其条目文本与 ans/CHECKLIST 措辞不同（完整句 vs 精简），无法逐字比对；
#     故按「每公理的 MUST/SHOULD 条目计数」锁结构：SPEC 增删条目或改 level 即被拦。
#     纯措辞改动（不增删、不改 level）不被此项捕获，须由维护者保证（见 GOVERNANCE / CLAUDE.md）。
spec_parts = re.split(r"^### 公理", spec, flags=re.M)[1:]
check("SPEC 公理块==4", len(spec_parts) == 4, f"找到 {len(spec_parts)} 个公理块")
for i, ax in enumerate(ans["axioms"]):
    if i >= len(spec_parts):
        break
    seg = spec_parts[i]
    a, b = seg.find("规范要求"), seg.find("反模式")
    body = seg[a:b] if a >= 0 and b >= 0 else ""
    sm = ssh = 0
    for ln in body.splitlines():
        t = ln.strip()
        if not t.startswith("- "):
            continue
        if "**MUST**" in t:
            sm += 1
        elif "**SHOULD**" in t:
            ssh += 1
    am = sum(1 for c in ax["clauses"] if c["level"] == "MUST")
    ash = sum(1 for c in ax["clauses"] if c["level"] == "SHOULD")
    check(f"{ax['id']} SPEC 条目数 ans==SPEC", (sm, ssh) == (am, ash),
          f"SPEC={sm}M/{ssh}S vs ans={am}M/{ash}S")

# ================= 报告 =================
status = "pass" if not errors else "fail"
report = {"status": status, "errors": errors, "warnings": warnings,
          "checks": checks, "clauseCount": len(ans_ids), "version": ans["version"]}

print(json.dumps(report, ensure_ascii=False, indent=2))

if "--json" not in sys.argv:
    line = "─" * 48
    passed = sum(1 for c in checks if c["ok"])
    print(line, file=sys.stderr)
    print(f"ans-lint: {status.upper()}  ({passed}/{len(checks)} checks)  v{ans['version']}", file=sys.stderr)
    for c in checks:
        if not c["ok"]:
            print(f"  ✗ {c['name']}: {c['detail']}", file=sys.stderr)
    for w in warnings:
        print(f"  ⚠ {w}", file=sys.stderr)
    print(line, file=sys.stderr)

sys.exit(0 if status == "pass" else 1)
