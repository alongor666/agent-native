# CLAUDE.md — agent-native 规范仓工作规则

本仓制定《Agent-Native 软件设计规范》。**工作方式本身必须遵守规范定义的四公理**（以身作则）。

## 动手前

先读 `STATUS.md`（现状/待办/决策/不变量）→ `SPEC.md`（规范本体）→ `CHECKLIST.md`（验收）。
有方向分叉先问，再动手。

## 不变量（改 SPEC 别破坏）

- **四公理互相独立**：砍掉任一根，其余无法补全。新增内容不得让它们耦合。
- **规范自身遵守它自己**：`SPEC.md` 是单一真源；`CHECKLIST.md` 从 SPEC 的 MUST 派生 —— 改 SPEC 必须同步 CHECKLIST（公理一）。
- **RFC 2119 规范语言**：normative 条目用 MUST/SHOULD/MAY，保持可判定合规，不退化为随笔。
- **文档分层**：README(人类) / CLAUDE(本仓 Agent) / SPEC(规范) / CHECKLIST(验收) / STATUS(状态)，各司其职不混写。

## 每次进展后

- 更新 `STATUS.md`：勾掉/新增待办、追加决策日志（状态外置，便于下个会话无缝接续 —— 公理三）。
- 实质决策记入 STATUS「决策日志」，带日期与一句理由。

## 验证

本仓暂无代码门禁；人工核对：改 SPEC 后 CHECKLIST 是否同步、四公理是否仍独立、normative 语言是否保持。
若后续加可执行校验（如 lint SPEC↔CHECKLIST 一致），即为本仓自身满足公理一②的体现。
