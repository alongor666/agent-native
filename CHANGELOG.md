# CHANGELOG — Agent-Native Specification (ANS)

依 [GOVERNANCE.md](./GOVERNANCE.md) §3.1 维护；版本跃迁规则见 GOVERNANCE §1。
格式参照 [Keep a Changelog](https://keepachangelog.com/)。

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
