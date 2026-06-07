# CLAUDE.md — agent-native 规范仓工作规则

本仓制定《Agent-Native 规范》(Agent-Native Specification, ANS)。**工作方式本身必须遵守规范定义的四公理**（以身作则）。

## 动手前

先读 `STATUS.md`（现状/待办/决策/不变量）→ `SPEC.md`（规范本体）→ `CHECKLIST.md`（验收）。
有方向分叉先问，再动手。

## 不变量（改 SPEC 别破坏）

- **四公理互相独立**：砍掉任一根，其余无法补全。新增内容不得让它们耦合。
- **规范自身遵守它自己**：`SPEC.md` 是单一真源；`CHECKLIST.md` 从 SPEC 的 MUST 派生 —— 改 SPEC 必须同步 CHECKLIST（公理一）。
- **RFC 2119 规范语言**：normative 条目用 MUST/SHOULD/MAY，保持可判定合规，不退化为随笔。
- **文档分层**：README(人类) / CLAUDE(本仓 Agent) / SPEC(规范) / CHECKLIST(验收) / ASSESSMENT(自评模板) / GOVERNANCE(治理演进) / CHANGELOG(变更日志) / STATUS(状态)，各司其职不混写。
- **演进走 GOVERNANCE**：normative 变更须按 `GOVERNANCE.md` §3 流程（改 SPEC→同步 CHECKLIST/ASSESSMENT→记 STATUS→登记 CHANGELOG→定版打 tag）。

## 每次进展后

- 更新 `STATUS.md`：勾掉/新增待办、追加决策日志（状态外置，便于下个会话无缝接续 —— 公理三）。
- 实质决策记入 STATUS「决策日志」，带日期与一句理由。

## 验证

改动后跑 `python3 tools/ans-lint.py`（exit 0=一致，≠0 阻断）：校验 `ans.json` 与 SPEC/CHECKLIST/ASSESSMENT/changelog 派生一致。
另人工核对：四公理是否仍独立、normative 语言是否保持。lint 即本仓自身满足公理①②的体现。
