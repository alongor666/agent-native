# CHANGELOG — Agent-Native Specification (ANS)

依 [GOVERNANCE.md](./GOVERNANCE.md) §3.1 维护；版本跃迁规则见 GOVERNANCE §1。
格式参照 [Keep a Changelog](https://keepachangelog.com/)。

## [0.2.0] — 2026-06-07 · Candidate

阶段跃迁：Draft → Candidate（结构冻结、进入候选期）。无 normative 条目增删，向后兼容。

### Changed
- 成熟阶段 **Draft → Candidate**。GOVERNANCE §2 退出条件满足：四公理稳定、CHECKLIST/SPEC 全条目对齐、参考实现 `nfra-penalty-pipeline` 按 ASSESSMENT 模板实测 **L2**（≥1 参考实现验证）。
- `GOVERNANCE.md`：明确阶段跃迁版本规则（阶段推进计 MINOR；Candidate→Stable 发 1.0.0）+ `0.x` Candidate 与破坏性变更的关系澄清。
- `tools/ans-lint.py` / `changelog.json`：支持「无 `entryId` 的元数据变更条目」以表达阶段跃迁等非条目变更。

## [0.1.0] — 2026-06-07 · Draft

首个草案版本，结构成型。

### Added
- 四公理（① 确定性契约 / ② 可验证闭环 / ③ 可恢复状态 / ④ 安全边界），各含 MUST/SHOULD 规范条目与 1 正 1 反例。
- §3 一致性：四问验收（机械可执行）+ L0–L3 成熟度分级。
- §4 与现有工作的关系：MCP / OpenAPI / llms.txt / AGENTS.md / 声明式 IaC / SemVer / OpenTelemetry / SLSA 精确投影到具体 MUST/SHOULD + 「标准 × 命中条目」对照表，坐实四公理互相独立。
- 附录 A：跨 6 类项目 × 四公理落地对照表。
- `CHECKLIST.md`：派生自 SPEC 的验收清单，四问 + 每条 MUST 配「→ 验证」机械判定法。
- `ASSESSMENT.md`：成熟度自评模板，确定性判级算法 + 缺口清单生成 + 示例。
- `GOVERNANCE.md`：治理与演进（SemVer 化、成熟阶段、维护流程、发布形态、兼容性声明）。
- `LICENSE`：CC-BY-4.0。
- **机器可读契约 `ans.json`**（19 条 normative 条目 + 四问 + 级别）+ 一致性门禁 `tools/ans-lint.py`（语义化退出码，经正反验证）+ `changelog.json` / `compatibility.json`。本仓自身据此达成公理① A1.1/A1.2。

### Notes
- 借鉴 Codex / Claude Code / MCP 底层机制校准了 ①规则分层、②失败分类含错误域+可重试、③运行期约束须外置、④硬边界须外部机制强制 四条。
