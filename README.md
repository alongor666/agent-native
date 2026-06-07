# Agent-Native Specification (ANS)

一份**与技术栈、领域无关**的规范：当软件的开发者与消费者都是 AI Agent 时，如何设计软件。

> 中文名《Agent-Native 规范》· 授权 [CC-BY-4.0](./LICENSE)

## 文档（按读者分层）

| 文件 | 给谁 | 内容 |
| --- | --- | --- |
| `SPEC.md` | 规范读者 | 规范本体：四公理 + 验收 + 成熟度 + 跨类型对照（RFC 2119 规范语言）|
| `CHECKLIST.md` | 验收者 / Agent | 四问 + 每公理 MUST 逐条清单，每条配「→ 验证」机械判定法（派生自 SPEC，须同步）|
| `ASSESSMENT.md` | 自评者 / Agent | 成熟度自评模板：填四问 + 勾选 MUST → 机械输出 L0–L3 + 缺口清单（派生）|
| `GOVERNANCE.md` | 维护者 / 采用者 | 治理与演进：SemVer 化、成熟阶段、维护流程、发布形态、兼容性声明 |
| `CHANGELOG.md` | 采用者 / Agent | 版本变更日志（GOVERNANCE §3.1）|
| `STATUS.md` | 维护者 / 新会话 | 当前状态、待办、决策日志、不变量（**新会话先读这个**）|
| `CLAUDE.md` | 在此仓工作的 Agent | 本仓工作规则 |
| `KICKOFF.md` | 你 | 一键复制的首次会话指令 |
| `LICENSE` | 所有人 | CC-BY-4.0：自由传播与改编，须署名 |

## 一句话

> 单一真源 → 自动派生 → 门禁锁一致 → 机器可读契约暴露 → 行动闭环反馈 → 状态可恢复 → 危险操作设界。

## 四公理

1. **确定性契约** — 消灭歧义：接口/数据/版本/能力机器可判定、自描述、单一真源。
2. **可验证闭环** — 行动必有机器可读结果与失败原因，Agent 方能自纠。
3. **可恢复状态** — 中断不致命：状态外置、幂等、可断点续跑。
4. **安全边界** — 快速试错不造成不可逆伤害：危险操作显式确认/可回滚。

## 如何消费 ANS（其他项目这样用）

- **机器可读契约**：读 [`ans.json`](./ans.json) —— 四公理 + 19 条 normative 条目（每条含 `level`/`text`/`verify`）+ 四问 + 成熟度级别。Agent 仅靠它即可消费，无需读散文。
- **自评成熟度**：复制 [`ASSESSMENT.md`](./ASSESSMENT.md) 填四问 + 勾 MUST → 机械得出 L0–L3 + 缺口清单。
- **稳定引用**：按条目 id（如 `A1.3`）+ git tag（如 `v0.1.0`）引用；`git show v0.1.0:ans.json` 取不可变快照。
- **判断版本是否破坏**：比 SemVer + 读 [`compatibility.json`](./compatibility.json) 的 `breaking` 字段（见 GOVERNANCE §5）。
- **校验一致性**：`python3 tools/ans-lint.py`（exit 0 = ans.json 与 SPEC/CHECKLIST/ASSESSMENT 一致）。

## 状态

v0.1.0 · Draft。参考实现：[`nfra-penalty-pipeline`](../nfra-penalty-pipeline)（数据产线象限，①②④ 已落地、③ 本达标）。

本项目**以身作则**遵守它自己定义的规范（SPEC 是单一真源，CHECKLIST 派生，STATUS 状态外置）。
