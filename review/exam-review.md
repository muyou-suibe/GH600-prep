# Exam Review

考前用作"模拟考复盘模板"，考后填成真正的"考后复盘"。GH-600 是 beta 考试，成绩会在 beta 结束后延迟约 8 周公布，所以复盘要先基于自我感觉写一版，成绩公布后再补一版"结果对照"。

## 基本信息

- 类型：模拟考 / 正式考试
- 日期：
- 用时：
- 自我感觉分数区间：
- 官方成绩（正式考试，成绩公布后补）：

## 按 Domain 自评

| Domain | Weight | 我能解释清楚的内容 | 我还不稳定的内容 |
|---|---:|---|---|
| 1. Agent architecture and SDLC | 15-20% | | |
| 2. Tools, MCP, environment | 20-25% | | |
| 3. Memory, state, execution | 10-15% | | |
| 4. Evaluation, error analysis | 15-20% | | |
| 5. Multi-agent coordination | 15-20% | | |
| 6. Guardrails and accountability | 10-15% | | |

## 高频场景回顾

| Scenario | Key Decision | Risk | Correct Action |
|---|---|---|---|
| | | | |

## 结果对照（成绩公布后填写）

- 官方是否通过：
- 和自评差距最大的 domain：
- 差距原因：

## 下一步

- [ ] 把新发现的薄弱点写回 `practice/mistakes.md`
- [ ] 把新发现的场景补进 `practice/scenarios.md`
- [ ] 补充或修正 `notes/` 对应文件
- [ ] 把这次复盘中反复验证有效的判断逻辑，沉淀进 `skill/SKILL.md`

## GH-600 Demo 总复盘

### 我完成了什么

我用 6 个 demo 验证了 GH-600 的 6 个核心考试域：

1. Agent Architecture and SDLC
2. Tools, MCP, and Environment
3. Memory, State, and Execution
4. Evaluation, Error Analysis, and Optimization
5. Multi-Agent Coordination
6. Guardrails and Accountability

每个 demo 都按照同一个流程完成：

- 创建 demo
- 运行初始版本
- 修改参数做实验
- 恢复成学习版本
- 写入 notes
- commit
- push 到 GitHub

### 1. Agent Architecture and SDLC

对应 demo：

`demos/01-agent-architecture/demo.py`

核心结论：

agent 不应该一收到任务就直接执行。  
它应该先明确：

- 任务目标
- 输入材料
- 预期输出
- 执行步骤
- 成功标准

如果涉及正式动作，必须先等待人工审批。

考试关键词：

- planning vs execution
- success criteria
- human-in-the-loop
- structured plan
- reviewable artifacts

### 2. Tools, MCP, and Environment

对应 demo：

`demos/02-tools-and-permissions/demo.py`

核心结论：

agent 的能力边界由 tools 配置决定。  
不能给所有 agent 默认开放全部工具，应该按照职责分配最小必要权限。

考试关键词：

- tool scoping
- tool permissions
- least privilege
- MCP server
- execution context

### 3. Memory, State, and Execution

对应 demo：

`demos/03-memory-state/demo.py`

核心结论：

agent 可以使用 memory，但不能永久相信 memory。  
memory 必须考虑：

- scope
- freshness
- relevance
- risk

过期信息必须重新验证。

考试关键词：

- repository-level facts
- user-level preferences
- stale context
- context drift
- state continuity

### 4. Evaluation, Error Analysis, and Optimization

对应 demo：

`demos/04-evaluation/demo.py`

核心结论：

agent 输出后，不能只看“有没有产出”，还要看是否满足预先定义的成功标准。

失败后要分类原因：

- 推理或计划失败
- 缺少评估产物
- 操作安全失败
- 工具误用

考试关键词：

- evaluation signals
- root cause analysis
- workflow artifacts
- logs
- optimization

### 5. Multi-Agent Coordination

对应 demo：

`demos/05-multi-agent/demo.py`

核心结论：

多 agent 协调的核心不是让多个 agent 同时跑，而是明确职责边界、隔离修改范围、检测冲突并保留审计记录。

考试关键词：

- multi-agent coordination
- agent isolation
- overlapping changes
- duplicated effort
- handoff
- auditability

### 6. Guardrails and Accountability

对应 demo：

`demos/06-guardrails/demo.py`

核心结论：

低风险动作可以自动执行，高风险动作必须被 guardrails 拦住，直到人工审批。

高风险关键词：

- production
- default branch
- merge
- secret
- delete
- compliance
- irreversible

考试关键词：

- guardrails
- human approval
- autonomy level
- accountability
- controlled execution path
- rollback

## 我的考试判断口诀

遇到 GH-600 场景题时，先问：

1. agent 有没有先输出计划？
2. 输入、输出、成功标准是否明确？
3. agent 使用的工具是否超过职责范围？
4. memory 是否过期或作用域不对？
5. 输出是否有测试、日志、扫描、PR、计划等 artifact？
6. 多 agent 是否修改同一文件或重复工作？
7. 高风险动作是否需要人工审批？
8. 是否有审计记录和回滚路径？

一句话总结：

agent 可以加速 SDLC，但必须被计划、权限、评估、隔离、护栏和审计机制约束。