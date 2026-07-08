# Domain 5: Multi-Agent Coordination

权重：15-20%

## 核心问题

如何管理多个 agents 的协作、隔离、冲突、交接、可观测性、恢复和生命周期。

## 必须掌握

- orchestration patterns
- parallel execution
- agent isolation
- overlapping code changes
- duplicated effort
- contradictory outputs
- logs and operational signals
- reviewable and auditable artifacts
- key decisions
- handoffs
- outcomes
- ad hoc analysis
- failed agent tasks
- partial agent tasks
- suspended agent tasks
- recovery pattern
- rollback
- human intervention
- adding agents
- updating agents
- replacing agents
- decommissioning agents

## 复习问题

- 多 agent 并行修改同一代码区域时如何处理？
- 如何记录 agent handoff？
- 如何在不中断工作流的情况下替换 agent？

## Demo 验证：多智能体协调和冲突检测

### 我做了什么

我创建并运行了：

`demos/05-multi-agent/demo.py`

这个 demo 模拟了三个智能体：

- `frontend_agent`：负责前端页面和模板
- `docs_agent`：负责文档和安装说明
- `security_agent`：负责安全检查和依赖风险

每个智能体都有自己计划修改的文件范围。

### 我观察到的结果

初始版本中：

```python
frontend_agent -> app.py
security_agent -> app.py

两个智能体都要修改 app.py，所以程序输出：
发现冲突：app.py: frontend_agent 与 security_agent 存在修改冲突
当我临时把 security_agent 的文件范围从 app.py 改成 security.py 后，输出变成：
未发现冲突。
恢复为 app.py 后，冲突重新出现。
我的理解
多 agent 协调的风险不是 agent 数量本身，而是职责和修改范围重叠。
如果多个 agent 同时修改同一个文件，可能出现：
互相覆盖代码
重复完成同一任务
输出结论矛盾
PR 难以审查
出问题后难以追踪责任
所以多 agent 工作流需要：
明确职责边界
限定文件或任务范围
分支隔离
冲突检测
交接记录
审计日志
必要时人工介入
对 GH-600 的意义
这个 demo 对应 GH-600 中的几个考点：
multi-agent coordination
agent isolation
overlapping changes
duplicated effort
conflict detection
handoff
auditability
考试中如果遇到多个 agent 并行工作，要优先考虑是否存在任务范围重叠、文件冲突、输出矛盾，以及是否需要隔离、日志和人工协调。