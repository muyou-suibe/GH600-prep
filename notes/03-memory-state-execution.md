# Domain 3: Memory, State, and Execution

权重：10-15%

## 核心问题

如何管理 agent 的短期记忆、长期记忆、外部记忆、状态持久化和上下文漂移。

## 必须掌握

- short-term memory
- long-term memory
- external memory
- task-relevant memory scope
- memory expiration
- pruning rules
- reset rules
- persistent task progress
- decision capture
- context drift detection
- state sharing
- conflicting context prevention
- stale context prevention

## 复习问题

- 什么信息应该进入长期记忆？
- 如何避免 agent 继续执行时偏离之前的决策？
- stale context 和 conflicting context 有什么区别？

## Demo 验证：Memory、State 和上下文连续性

### 我做了什么

我创建并运行了：

`demos/03-memory-state/demo.py`

这个 demo 模拟了三类记忆：

- repository memory：项目级事实，例如“运行测试使用 pytest”
- stale repository memory：过期项目事实，例如“部署仍使用旧的 staging 脚本”
- user memory：用户级偏好，例如“用户偏好简洁的 Pull Request 摘要”

### 我观察到的结果

初始版本中，第二条 memory 的 `last_validated` 是 45 天前，因此超过 28 天有效期，被判断为：

```text
已过期: [repository] 部署仍使用旧的 staging 脚本。

当我临时把 45 天改成 7 天后，它变成：
有效: [repository] 部署仍使用旧的 staging 脚本。
恢复为 45 天后，它再次被判断为已过期。
我的理解
agent 可以使用 memory，但不能永久相信 memory。
一条 memory 是否可以使用，至少要看：
scope：它属于 repository、user，还是其他外部上下文
freshness：最近是否验证过
relevance：是否和当前任务相关
risk：如果信息过期，会不会导致错误操作
repository memory 适合保存项目事实，例如测试命令、构建方式、架构约定。
user memory 适合保存用户偏好，例如输出风格、PR 摘要偏好。
state 更偏向当前任务进度，例如已经完成哪一步、下一步是什么。
对 GH-600 的意义
这个 demo 对应 GH-600 中的几个考点：
agent memory
repository-level facts
user-level preferences
state continuity
stale context
context drift
考试中如果遇到 agent 使用历史信息的场景，不能默认相信旧信息。应该优先考虑重新验证、限制作用域、删除过期信息或要求人工确认。