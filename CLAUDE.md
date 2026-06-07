# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

本仓制定《Agent-Native 规范》(Agent-Native Specification, ANS) —— 一份技术栈/领域无关的规范：当软件的开发者与消费者都是 AI Agent 时如何设计软件。**工作方式本身必须遵守规范定义的四公理**（以身作则）。

## 这是什么仓

一个**规范文档仓**，不是应用代码项目。唯一可执行物是一致性门禁脚本 `tools/ans-lint.py`（零依赖 Python3）。产物是 Markdown 规范 + 机器可读契约 JSON。

## 架构大图（读多文件才懂的部分）

**单一真源 → 派生 → 门禁锁一致**，这是全仓的组织原则，也是它对自身公理①的 dogfood：

- `SPEC.md` 是**唯一真源**（RFC 2119 normative 文本，四公理 + 每条 MUST/SHOULD + 正反例）。
- 三个**派生物**必须与 SPEC 一致：
  - `CHECKLIST.md` —— 验收清单，每条 MUST 配「→ 验证」机械判定法；条目 text 是权威文案。
  - `ASSESSMENT.md` —— 成熟度自评模板，条目带稳定 id `A{公理}.{序}`（A1.1–A4.4）+ `[MUST]/[SHOULD]` 标注 + 确定性判级算法。
  - `ans.json` —— 机器可读契约（19 条 normative 条目，clause `text` 与 CHECKLIST **逐字一致**、`id` 与 ASSESSMENT 一致）。供外部项目零散文消费。
- `tools/ans-lint.py` 锁上述一致性：校验 ans.json ↔ SPEC/CHECKLIST/ASSESSMENT/changelog 的条目集合、level、数量、版本、级别定义。**任一处漂移即 exit 1**。
- 治理层：`GOVERNANCE.md`（规范自身的 SemVer/阶段/演进流程/兼容性）；`changelog.json` + `compatibility.json` 是版本变更的机读形态。

**最易踩的依赖链**：改 `SPEC.md` 的任一 normative 条目，必须同步改 `CHECKLIST.md` 对应行（text 逐字）+ `ASSESSMENT.md` 勾选项与 `MUST(k)` 集合 + `ans.json` clause + `changelog.json`，然后跑 lint。漏任一处，lint 会拦。

四公理（互相独立，由「人类 vs Agent 认知差异」降秩得出）：① 确定性契约 / ② 可验证闭环 / ③ 可恢复状态 / ④ 安全边界。成熟度 L0–L3 见 SPEC §3。

## 命令

本仓无传统测试框架，`ans-lint` 即「测试」：

```bash
python3 tools/ans-lint.py          # 一致性门禁；exit 0=一致，≠0=阻断（发版前 MUST 跑）
python3 tools/ans-lint.py --json   # 仅机读 JSON 报告（stdout），不打人读摘要
ANS_DIR=/path/to/copy python3 tools/ans-lint.py   # 对副本跑，用于负向测试（验证门禁能检出篡改）

git tag -a vX.Y.Z -m "..."         # 发版（GOVERNANCE §4 阶段一 MUST）
git show vX.Y.Z:ans.json           # 取某版不可变快照（外部消费者引用方式）
```

## 动手前

先读 `STATUS.md`（现状/待办/决策/不变量）→ `SPEC.md`（规范本体）→ `CHECKLIST.md`（验收）。有方向分叉先问，再动手。

## 不变量（改 SPEC 别破坏）

- **四公理互相独立**：砍掉任一根，其余无法补全。新增内容不得让它们耦合。
- **单一真源**：`SPEC.md` 是真源；`CHECKLIST.md`/`ASSESSMENT.md`/`ans.json` 从它派生 —— 改 SPEC 必须同步三者并通过 lint（公理①）。
- **RFC 2119 规范语言**：normative 条目用 MUST/SHOULD/MAY，保持可判定合规，不退化为随笔。
- **文档分层**：README(人类) / CLAUDE(本仓 Agent) / SPEC(规范) / CHECKLIST(验收) / ASSESSMENT(自评模板) / GOVERNANCE(治理演进) / CHANGELOG(变更日志) / STATUS(状态)，各司其职不混写。
- **演进走 GOVERNANCE**：normative 变更须按 `GOVERNANCE.md` §3 流程（改 SPEC→同步派生物→跑 lint→记 STATUS→登记 CHANGELOG→定版打 tag）。

## 每次进展后

- 更新 `STATUS.md`：勾掉/新增待办、追加决策日志（状态外置，便于下个会话无缝接续 —— 公理③）。
- 实质决策记入 STATUS「决策日志」，带日期与一句理由。
