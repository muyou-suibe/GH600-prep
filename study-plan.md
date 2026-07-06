# Study Plan（3 天冲刺版）

## 前提说明

备考时间压缩到 3 天，原则不变，但阶段（Phase）改为按天（Day）排期，且必须按 domain 权重分配时间，不能 6 个 domain 平均用力。

## 学习原则

- 以官方考试域为主线，不按零散资料学习。
- 时间优先分配给高权重 domain：Domain 2（20-25%）> Domain 1 / 4 / 5（各 15-20%）> Domain 3 / 6（各 10-15%）。
- 每个主题至少形成"概念、场景、错题"三类记录，时间不够时优先保场景判断，不死磕纯概念背诵。
- 对 GitHub / Copilot / MCP / agents 的英文术语保留英文，中文解释要准确。

## Day 1：建地图 + 学高权重 domain（对应 `notes/`）

- [ ] 阅读 GH-600 认证页面和学习指南，建好 6 个 domain 的 notes 文件框架
- [ ] 精学 Domain 2（Tools, MCP, environment，20-25%）→ 写完 `notes/02-tools-mcp-environment.md`
- [ ] 精学 Domain 1（Agent architecture and SDLC，15-20%）→ 写完 `notes/01-agent-architecture-sdlc.md`
- [ ] 精学 Domain 4（Evaluation, error analysis, optimization，15-20%）→ 写完 `notes/04-evaluation-error-analysis-optimization.md`
- [ ] 当天结束前，每个学完的 domain 至少回答一遍对应 notes 里的"复习问题"

## Day 2：学剩余 domain + 动手实践（对应 `notes/` + `practice/`）

- [ ] 学 Domain 5（Multi-agent coordination，15-20%）→ 写完 `notes/05-multi-agent-coordination.md`
- [ ] 学 Domain 3（Memory, state, execution，10-15%）→ 写完 `notes/03-memory-state-execution.md`
- [ ] 学 Domain 6（Guardrails and accountability，10-15%）→ 写完 `notes/06-guardrails-accountability.md`
- [ ] 在 `practice/scenarios.md` 记录 custom instructions / custom agents / MCP server 的动手实践（哪怕只是简单跑通一次）
- [ ] 用 `practice/scenarios.md` 里的出题 prompt，对 6 个 domain 各自测 5-10 题
- [ ] 把做错、猜对、不确定的题记录进 `practice/mistakes.md`，标注 Root Cause

## Day 3：模拟考 + 查漏补缺 + 考前冲刺（对应 `practice/` + `review/`）

- [ ] 上午：做一套完整模拟题（无则用自测题合并成一套），严格计时 120 分钟
- [ ] 对照 `practice/mistakes.md` 按 domain 统计薄弱点，优先回炉 Domain 2 / 4 / 5
- [ ] 重点过一遍高频场景判断和易混概念（谁该 human approval、什么算 least privilege、reasoning error 和 tool misuse 怎么区分等）
- [ ] 考前 1-2 小时：只看 `practice/mistakes.md` 的错题表和易混概念对照，不再学新内容
- [ ] 考试结束后（当天或次日）：填写 `review/exam-review.md`
- [ ] 把这次复盘中反复验证有效的判断逻辑，沉淀进 `skill/SKILL.md`
