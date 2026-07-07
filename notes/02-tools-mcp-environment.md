# Domain 2: Tools, MCP, and Environment Interaction

权重：20-25%

这是 GH-600 权重最高的考试域之一。

## 核心问题

如何为 agents 选择工具、配置 MCP server、限制权限，并让 agent 在开发环境、仓库、分支和 CI workflow 中可靠运行。

## 必须掌握

- required tools identification
- agent tool configuration
- tool permissions
- MCP server as agent tool
- GitHub remote MCP server
- MCP registry
- MCP allowlist
- execution context
- repository scope
- CI workflow invocation
- branch-based scope
- autonomous operations
- branch and pull request creation
- environment constraints
- error handling
- retry mechanism
- rollback
- escalation path
- traceability and accountability

## 复习问题

- MCP allowlist 的作用是什么？
- agent tool permission 应该如何限定？
- agent 在 CI workflow 中被调用时，要考虑哪些执行上下文？
- agent 可以自主创建 PR 时，需要哪些防护和审计？
## Demo 验证：工具权限和最小权限原则

### 我做了什么

我创建并运行了：

`demos/02-tools-and-permissions/demo.py`

这个 demo 模拟了三个不同职责的智能体：

- `researcher`：研究型智能体，只能读取资料和搜索仓库
- `editor`：编辑型智能体，可以读取资料、搜索仓库和修改文件
- `release_manager`：发布型智能体，可以读取资料和创建 PR，但不能直接修改文件

### 我观察到的结果

安全版本中，`researcher` 没有 `edit_file` 权限，所以输出：

```text
已拒绝：researcher 不能使用工具 edit_file
当我临时给 researcher 增加 edit_file 权限后，输出变成：
已允许：researcher 使用工具 edit_file
恢复最小权限后，researcher 再次被拒绝使用 edit_file。
我的理解
agent 的能力边界由工具配置决定。
如果一个 agent 被配置了某个工具，它就可能执行对应动作。
所以不应该给所有 agent 默认开放全部工具，而应该按照职责分配最小必要权限。
研究型 agent 应该只读；编辑型 agent 才能修改文件；发布型 agent 可以创建 PR，但不应该直接绕过编辑和审查流程。
对 GH-600 的意义
这个 demo 对应 GH-600 中的几个考点：
tool scoping
tool permissions
least privilege
execution context
guardrails
考试中如果遇到 agent 工具配置场景，优先考虑：
agent 是否真的需要这个工具
工具是否有写权限或高风险能力
是否应该把工具限制在特定 agent 上
是否需要审批、日志或隔离机制