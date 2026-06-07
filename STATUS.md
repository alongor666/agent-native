# STATUS — Agent-Native 规范项目

> 新会话先读本文件。状态外置于此，便于任意会话无缝接续（公理三的自我实践）。

## 现状（2026-06-07）

- **待办 1–8 全部完成**，规范 **v0.2.0 · Candidate** —— 结构冻结、进入候选期。
- `SPEC.md`：四公理（各含 MUST/SHOULD + 1 正 1 反例）+ 四问验收 + L0–L3 成熟度 + §4 标准精确映射（对照表）+ 附录 A 跨 6 类对照表。命名 **ANS = Agent-Native Specification**，授权 CC-BY-4.0。
- 派生与配套：`CHECKLIST.md`（每条配「→ 验证」）、`ASSESSMENT.md`（确定性判级模板）、`GOVERNANCE.md`（治理演进）、`CHANGELOG.md`、`LICENSE`。
- 四条规范条目经 **Codex/Claude Code/MCP 调研**校准（见决策日志）。
- 参考实现 `../nfra-penalty-pipeline`（数据产线象限）：按 ASSESSMENT 模板实测 **L2（闭环就绪）**，sat=[T,T,T,F]，距 L3 仅差 A4.1（外发 Release 无确认/回滚）。模板捕捉到该仓自评 L3 时忽略的安全边界缺口 → 自评模板可用且有判别力。
- 第 2 个独立项目 `../preknow_shanxi`（组织人员分析 + 知识库，nfra 的消费方）：实测 **L0**，sat=[F,T,T,F]——②③全绿却因无数据集版本兼容声明（A1.3）卡在公理①、停 L0（前缀规则"跳级不升级"实例）。补 A1.3 即跳 L1。
- 机器可读契约 `ans.json` + 门禁 `tools/ans-lint.py`（正反验证通过，26/26 checks）已就位 → 本仓自身**达 L1**（机器可读契约 + 派生锁一致）；②③亦满足（lint 作为唯一操作返回机读结果+语义退出码、状态全外置）；④对纯文档仓语义弱（git 提供回滚/审计）。
- **已发布 v0.1.0（Draft）→ v0.2.0（Candidate）**（commit + 注解 tag）。

### ANS 自身成熟度自评（dogfood）

| 公理 | sat | 依据 |
| --- | --- | --- |
| ① 确定性契约 | ✓ | `ans.json` 机读契约；SPEC 单一真源 + CHECKLIST/ASSESSMENT/ans.json 派生 + lint 锁一致；SemVer + changelog/compatibility |
| ② 可验证闭环 | ✓ | lint 返回机读 JSON 报告 + 语义化退出码；失败按 check name 可分类；确定性可复现 |
| ③ 可恢复状态 | ✓ | 状态全外置于文件（STATUS/ans.json/…）；lint 无状态幂等可重跑；约束在持久配置非对话 |
| ④ 安全边界 | ～ | 纯文档仓无不可逆操作；git 版本控制提供回滚与审计。语义偏弱，不强主张 |

结论：**稳达 L1**，①②③ 满足可论 L2；④ 对本类项目语义弱故不冒进主张 L3。

## 待办（按优先级）

1. [x] 起正式名与缩写：**Agent-Native Specification (ANS)**；LICENSE = CC-BY-4.0。已同步 SPEC/README/CLAUDE/KICKOFF。
2. [x] 完善 `CHECKLIST.md`：四问 + 每条 MUST 均配「→ 验证」一句（技术无关的机械判定法），可当评分脚本读。SPEC 的 MUST 未改，公理一一致性保持。
3. [x] 每公理补 1 正 1 反例（嵌入对应公理块，技术无关）；并据 Codex/Claude Code/MCP 调研校准四条规范条目，CHECKLIST 已同步。
4. [x] 坐实「与现有标准映射」：SPEC §4 重写为「标准 × 命中的 MUST/SHOULD」对照表 + 逐标准映射 + 互相独立结论（MCP/OpenAPI/llms.txt/AGENTS.md/IaC/SemVer/OTel/SLSA）。
5. [x] 成熟度自评模板：新建 `ASSESSMENT.md`（四问 + 逐 MUST 勾选 → 确定性判级算法 → L0–L3 + 缺口清单，附示例）。
6. [x] 发布形态与演进规则：新建 `GOVERNANCE.md`（规范自身 SemVer 化、Draft/Candidate/Stable 阶段、维护流程、分阶段发布、兼容性声明）+ `CHANGELOG.md`；SPEC 版本规整为 0.1.0(Draft)。
7. [x] **发布 v0.1.0**：commit 本批改动 + 打注解 tag `v0.1.0`（GOVERNANCE §4 阶段一 MUST）。
8. [x] 机器可读契约 + 自动门禁：新建 `ans.json`（19 条 + 四问 + 级别）、`tools/ans-lint.py`（一致性门禁，正反验证均通过）、`changelog.json`、`compatibility.json`。本仓自身据此满足公理① A1.1/A1.2。
9. [ ] **升 Stable（1.0.0）**：§2 退出条件满 2/3——无 MAJOR 争议 ✓ + ≥2 独立项目自评 ✓（nfra L2 / preknow L0）；**待**公开反馈期 ≥ 一迭代周期无阻断异议（需外部采用/反馈，非本地可即时完成）。

## 决策日志

- 2026-06-07 规范与任何项目**解耦**，独立仓维护（不放进 nfra 仓），以求全球通用。
- 2026-06-07 采用 **RFC 2119** 规范语言，做成可判定合规的 spec 而非随笔。
- 2026-06-07 四公理由「人类 vs Agent 认知差异」**降秩**得出（确定性/反馈/恢复/安全），四者互相独立。
- 2026-06-07 本仓**以身作则**遵守自身规范：SPEC 单一真源、CHECKLIST 派生同步、STATUS 状态外置。
- 2026-06-07 正式名定为 **Agent-Native Specification (ANS)**：去掉 "Software"，范围不限软件、更通用；中文名《Agent-Native 规范》。
- 2026-06-07 LICENSE 选 **CC-BY-4.0**：规范文档应允许自由传播与改编、署名即可，与 W3C/IETF 风格 spec 一致（非代码故不用 MIT）。
- 2026-06-07 待办7/8完成：建 `ans.json`（机器可读契约，SPEC 的结构化投影）+ `tools/ans-lint.py`（零依赖、语义化退出码、正反验证：正向 21/21 PASS、负向篡改 level/删条目均 exit 1）+ `changelog.json`/`compatibility.json`。门禁从 GOVERNANCE「人工核对」升级为自动 lint。本仓自此满足公理① A1.1（机读契约）/A1.2（派生锁一致），回应「他人如何消费 ANS」：读 ans.json + 填 ASSESSMENT 自评 + 按 tag/id 引用 + 比 compatibility.json。已 commit + 打 tag v0.1.0。
- 2026-06-07 第4/5/6项经 workflow 三 agent 并行起草、主控审校后落地：§4 改为「标准×命中 MUST」对照表；新建 ASSESSMENT.md（判级硬条件仅取 MUST、SHOULD 不降级，与 §3.2 对齐）；新建 GOVERNANCE.md（治理与 SPEC 正交故独立成文，发布渐进式先 git tag+版本化 Markdown，不过度工程化）；条目 id 0.x 期复用 ASSESSMENT 的 `A{公理}.{序}`、1.0 起内嵌。
- 2026-06-07 调研 **Codex / Claude Code / MCP** 底层机制（AGENTS.md/CLAUDE.md 分层加载、MCP 能力发现与双层错误、session resume/compaction、approval/permission modes、OS 沙箱），带来源。据此：①正反例**嵌入各公理块**（紧贴定义、保持单一真源，不另开 EXAMPLES.md）；②校准四条 —— ①规则分层（强制配置 vs 参考叙事）、②失败分类含错误域+可重试、③运行期约束/规则亦须外置（防上下文压缩丢失）、④硬边界须**外部机制强制**（AI 自检非唯一防线）。四公理独立性不变，CHECKLIST 同步。
- 2026-06-07 实跑参考实现 `nfra-penalty-pipeline` 自评（Explore agent 进仓逐条核证 14 判定点 → 套 §2 判级算法）：评级 **L2**，距 L3 差 A4.1（外发 Release 无确认/回滚）。该仓自评 L3、ANS 模板严判 L2，验证模板有判别力、判级算法可机械复现。此为 GOVERNANCE §2 Draft→Candidate 退出条件「≥1 参考实现验证」之证据其一。
- 2026-06-07 升 **Draft→Candidate**（发 v0.2.0）：§2 退出条件满足（四公理稳定 + CHECKLIST/SPEC 对齐 + nfra 参考实现实测 L2）。决策：阶段跃迁按"加稳定性保证"计 **MINOR**（已补 GOVERNANCE §1 版本规则）；changelog/lint 增「无 `entryId` 元数据变更条目」支持以表达非条目变更。`0.x` 期 Candidate 仍可 MINOR 破坏性修订，结构硬冻结待 `1.0.0` Stable。升 Stable 尚需 ≥2 独立项目自评通过。
- 2026-06-07 用 `preknow_shanxi` 做第 2 个独立项目自评：评级 **L0**（缺 A1.3 数据集版本兼容声明，虽②③全绿）。至此 §2「≥2 独立项目自评跑通」满足（nfra L2 + preknow L0，跨数据产线/知识库两域，模板均产出确定结论、含 L0 边界，判别力获证）。但升 Stable 三条退出条件仍缺第三条「公开反馈期 ≥ 一迭代周期无阻断异议」——规范新发布无外部反馈期，**暂不升 Stable**。
- 2026-06-07 PR#1 Codex review（P2）指出 `ans-lint` 未校验 SPEC 正文 → SPEC-only 的 MUST 增删/改 level 会漏过、文档「lint 会拦」属过度承诺。已增强 lint：按**每公理 MUST/SHOULD 条目计数**锁 SPEC↔ans.json（删条目/改 level 即 exit 1，负向验证通过、正向 26/26）；并修正 CLAUDE.md/GOVERNANCE 措辞——lint 锁条目结构，纯措辞逐字一致由维护者保证。

## 关键不变量

- 四公理必须互相独立（砍一根其余无法补全）。
- SPEC 是单一真源；CHECKLIST 与 ASSESSMENT 均从它派生 —— 三者须始终一致（增删 MUST/SHOULD 必同步）。
- 演进按 GOVERNANCE §3 流程；normative 变更须登记 CHANGELOG 并按 §1 定版。
