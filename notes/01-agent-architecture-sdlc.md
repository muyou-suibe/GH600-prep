# Domain 1: Agent Architecture and SDLC

权重：15-20%

## 核心问题

如何把 agents 放入 SDLC，并清楚定义 agent 的输入、输出、成功条件、执行边界和人工审批点。

## 必须掌握

- agent 在 SDLC 中适合执行哪些步骤
- 常见 agent anti-patterns
- agent input / output / success criteria
- planning、reasoning、action 的边界
- structured plan 的作用
- agent plan validation
- approval before action
- observability and control
- autonomy level and guardrails

## 复习问题

- agent planning 和 agent execution 为什么要分开？
- 什么情况下应该阻止 agent 直接执行操作？
- 如何配置 agent 输出可检查的计划？
- 如何在不明显降低交付速度的前提下加入 human intervention？

## Demo 验证：先计划、再审批、后执行

### 我做了什么

我创建并运行了：

`demos/01-agent-architecture/demo.py`

这个 demo 模拟了一个智能体任务：

- 任务目标：创建部署检查清单
- 输入材料：`issue.md`、`service.yml`
- 预期输出：`deployment-checklist.md`
- 成功标准：包含回滚方案、列出负责人、包含验证步骤

### 我观察到的结果

第一次运行时，`approved` 默认为 `False`，所以执行被阻止：

```text
已阻止：执行前需要人工审批。
当我把下面两行注释掉：
# task.approved = True
# print(execute(task))
程序不会再输出“已执行”。
恢复这两行后：
task.approved = True
print(execute(task))
程序会输出：
已执行：生成 deployment-checklist.md
我的理解
这个 demo 说明：智能体可以先自动生成计划，但不应该在没有审批的情况下执行正式动作。
计划阶段应该包含：
任务目标
输入材料
预期输出
执行步骤
成功标准
执行阶段应该检查是否已经审批。没有审批时，系统应该阻止执行。
对 GH-600 的意义
这个 demo 对应 GH-600 中的几个考点：
planning vs execution
success criteria
human-in-the-loop
guardrails
reviewable artifacts
考试中如果遇到高风险智能体操作，例如修改生产配置、合并 PR、推送到受保护分支、访问敏感数据，应该优先考虑人工审批、权限限制和可审查记录。