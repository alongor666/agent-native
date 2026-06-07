# GOVERNANCE — Agent-Native 规范的治理与演进

> 本文件是**关于规范自身的契约**：版本编号、成熟阶段、维护流程、发布形态、兼容性声明。
> 与 `SPEC.md`（关于被规范物的契约）正交。规范本体的演进规则在此**单一真源**。
> 关键词 MUST/SHOULD/MAY 依 RFC 2119 解释。

## 1. 版本编号（规范自身用 SemVer）

ANS 规范文档以 `MAJOR.MINOR.PATCH` 标识（呼应公理① "版本兼容性机器可判定"，规范以身作则）。
版本跃迁的判定对象是**规范中的 normative 条目**——即 SPEC.md 内每一条含 MUST / MUST NOT / SHOULD / SHOULD NOT / MAY 的规则。

每条 normative 条目 **SHOULD** 有稳定标识：`0.x` 草案期采用 `ASSESSMENT.md` 的 `A{公理}.{序}` 体系作为事实 id（如 `A1.3` = 公理一第 3 条），SPEC 正文用关键词引用即可，不强制内嵌编号；自 `1.0.0` 起 normative 条目 **MUST** 内嵌稳定 id，使增删改可被逐条 diff。

判定规则（机器可判定，按 normative 条目集合的变化）：

| 跃迁 | 触发条件 | 对合规判定的影响 |
| --- | --- | --- |
| **MAJOR** | 删除任一 normative 条目，或将 SHOULD 升为 MUST，或收紧既有 MUST 的判定（旧合规项可能变不合规） | **破坏**：依旧版判定为合规的项目，在新版下可能不再合规 |
| **MINOR** | 新增 MUST / SHOULD 条目，或新增公理 / 成熟度级别，或将 MUST 降为 SHOULD（向后兼容地**加**约束或**放松**） | **兼容**：旧版合规项目在新版下结论不变或仅"未达更高要求"，原有判定不被推翻 |
| **PATCH** | 仅措辞澄清、修正笔误、补正反例 / 叙事，**不改变任何条目的合规判定** | **无**：同一项目在新旧版下判定完全一致 |

机器可判定法：以条目 id（或关键词）为键，对两版 normative 条目集合做 diff。
**删除条目 ⇒ MAJOR**；仅**新增条目** ⇒ MINOR（无删除）；集合不变、仅文本变 ⇒ PATCH。
RFC 2119 关键词的"升格"（SHOULD→MUST）等价于删除旧弱条目+新增强条目，按删除处理 ⇒ MAJOR；"降格"（MUST→SHOULD）按放松处理 ⇒ MINOR。

`0.x` 阶段（当前）：规范处草案期，MINOR 即可含破坏性变更；`1.0.0` 起严格执行上表。

**阶段跃迁的版本号**：成熟阶段推进（Draft→Candidate→Stable）本身不增删 normative 条目，但提升对消费者的稳定性承诺，按"向后兼容地加保证"计 **MINOR**——`Draft→Candidate` 发 MINOR（如 `0.1.x → 0.2.0`），`Candidate→Stable` 发 `1.0.0`。阶段跃迁登记变更日志时，其 `changes[]` 用 `{"change":"stage", ...}` 元数据条目（**无 `entryId`**，因无条目增删）；`ans-lint` 据此跳过 `entryId` 为空的元数据条目。

## 2. 成熟阶段（Draft / Candidate / Stable）

每个版本 **MUST** 标注成熟阶段，写入 SPEC.md 头部版本行。

| 阶段 | 含义 | 进入条件 | 退出条件 |
| --- | --- | --- | --- |
| **Draft 草案** | 结构可变，条目可大改 | 默认初始态 | 四公理稳定、CHECKLIST 与 SPEC 全条目对齐、≥1 个参考实现验证可用 ⇒ 升 Candidate |
| **Candidate 候选** | 冻结结构，仅修订措辞与补例，征集外部反馈 | 满足上行退出条件 | 在 Candidate 阶段无未决 MAJOR 争议、≥2 个独立项目按本规范自评通过、公开反馈期（**SHOULD** ≥ 一个迭代周期）无阻断性异议 ⇒ 升 Stable 并发 `1.0.0` |
| **Stable 稳定** | 生产可引用，破坏性变更受 §1 MAJOR 约束 | 满足上行退出条件 | 仅当出现根本性重构需求时由 MAJOR 跃迁进入新一轮 Candidate |

阶段**只进不退**（除非 MAJOR 重构）；降级 **MUST** 走 MAJOR 并在变更日志说明理由。

> `0.x` 期的 Candidate 表达"意图冻结、优先只改措辞"；若外部反馈暴露结构性缺陷，`0.x` 仍可按 §1 以 MINOR 做破坏性修订（不必 MAJOR）。结构的**硬冻结**自 `1.0.0` Stable 起生效——届时破坏性变更受 §1 MAJOR 严格约束。

## 3. 规范维护流程（normative）

任何对 SPEC.md 的改动 **MUST** 走以下流程（本仓已实践，此处固化为强制）：

1. **改 SPEC**：在 `SPEC.md` 增删改 normative 条目，保持条目 id 稳定。
2. **同步 CHECKLIST**：`CHECKLIST.md` 派生自 SPEC 的 MUST。改 SPEC 后 **MUST** 同步 CHECKLIST，使二者条目一一对应（公理①单一真源）。新增 MUST 必须配「→ 验证」一句。
3. **同步 ASSESSMENT 与 ans.json**：若增删 MUST/SHOULD 条目，**MUST** 同步 `ASSESSMENT.md` 的勾选项、`MUST(k)` 集合定义与 `ans.json` 的 clause。
4. **记 STATUS 决策日志**：实质决策 **MUST** 记入 `STATUS.md` 决策日志，带日期与一句理由（公理③状态外置）。
5. **登记变更日志**：每次 **normative 变更** **MUST** 在变更日志（§3.1）登记一条；纯 PATCH 的非 normative 改动 **MAY** 省略。
6. **定版与打标**：按 §1 判定版本跃迁，更新 SPEC 头部版本行；发布时 **MUST** 打 git tag（§4）。

门禁不变量：发布前 **MUST** 跑 `python3 tools/ans-lint.py`，确认 `ans.json` 与 SPEC（每公理 MUST/SHOULD 条目计数）、CHECKLIST、ASSESSMENT、changelog 一致（exit≠0 即阻断、不得发布）。lint 锁**条目结构**（计数/id/level/版本）；SPEC 正文的纯措辞逐字一致不在机器校验范围，由维护者保证。这条自动门禁正是本仓自身满足公理①「派生物自动校验锁一致」与公理②「机器可读结果 + 语义化退出码」的体现。

### 3.1 变更日志

变更日志 **MUST** 存在并随每次 normative 变更更新，**SHOULD** 同时具备人读与机器可读两种形态：

- 人读：`CHANGELOG.md`（Keep a Changelog 风格，按版本分节，列 Added / Changed / Removed）。
- 机器可读：`changelog.json`（**SHOULD**，本仓已提供），每条记录含 `version`、`bump`(major|minor|patch)、`date` 与 `changes[]`（每项 `entryId` + `change`：added|removed|tightened|relaxed|clarified）。

使消费者无需读散文即可程序化得知"哪条规则在哪版怎么变了"。

## 4. 发布形态（分阶段，不过度工程化）

推荐**渐进式**，按需要逐级升级，不超前建设：

- **阶段一（现在，MUST）**：**git tag + 版本化 Markdown**。每次发布打带注解 tag（`vMAJOR.MINOR.PATCH`，如 `v0.1.0`），SPEC 头部版本行与 tag 一致。零新增依赖、零构建、可离线 diff，对 Agent 消费者最友好（直接 `git show <tag>:SPEC.md`）。理由：规范本体就是几个 Markdown，tag 已提供不可变快照与可复现引用，足够。
- **阶段二（Candidate 后，SHOULD）**：由 Markdown 自动生成**静态站点**（锚点可深链到条目 id）。理由：稳定后需要稳定外链与条目级引用，但应**从 SPEC 自动派生**（公理①派生物自动生成），不手写第二真源。
- **阶段三（Stable 后，MAY）**：RFC 风正式文本 / 提交标准组织。仅当出现跨组织采用需求时再做，否则不引入。

非目标：发布形态 **MUST NOT** 制造第二真源——任何派生产物（站点 / PDF / RFC）皆从 SPEC.md 生成并可自动校验一致。

## 5. 兼容性声明（消费者如何程序化判断破坏）

消费者（含 Agent）**MUST** 能仅靠机器可读信息判断两版 ANS 是否破坏，无需读散文：

1. **SemVer 比较**：同 MAJOR ⇒ 向后兼容（旧合规结论在新版仍成立）；MAJOR 提升 ⇒ 可能破坏，**MUST** 复核。
2. **compatibility.json**（**SHOULD** 随每版发布）：声明本版与历史版的兼容关系，每条 **MUST** 含 `fromVersion`、`toVersion`、`breaking`(bool)、`removedEntryIds`[]、`tightenedEntryIds`[]。消费者读 `breaking` 即可分支；读 `removed*/tightened*` 即可定位"我依赖的哪条条目受影响"。
3. **退化判定**：若 `compatibility.json` 缺失，消费者 **MUST** 退回纯 SemVer 规则保守处理（跨 MAJOR 视为破坏）。

兼容性的唯一判定依据是 §1 的 normative 条目集合 diff —— 兼容声明 **MUST** 与该 diff 一致，不得手工放宽。

## 6. 与本仓文档分层的关系

本文件加入分层：README(人) / CLAUDE(本仓 Agent) / SPEC(规范本体) / CHECKLIST(验收) / ASSESSMENT(自评模板) / STATUS(状态) / **GOVERNANCE(治理与演进)** / LICENSE。
GOVERNANCE 治理"规范如何演进"，SPEC 治理"被规范物如何设计"，二者不互相内嵌。
