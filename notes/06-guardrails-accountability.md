# Domain 6: Guardrails and Accountability

权重：10-15%

## 核心问题

如何根据操作、安全和合规风险定义自治级别，配置 human-in-the-loop，执行最小权限，并要求高风险操作走显式授权或受控路径。

## 必须掌握

- autonomy levels
- operational risk
- security risk
- compliance risk
- responsible AI standards
- human judgment
- policy violation blocking
- least privilege
- scoped permissions
- controlled path
- irreversible changes
- compliance-sensitive changes
- speed versus risk reduction

## 复习问题

- 哪些 agent 操作必须 human approval？
- 如何定义 autonomy level？
- 什么是 least privilege 在 agent 工具使用中的体现？
- 如何避免审批太多导致交付速度下降？

## Demo 验证：Guardrails、风险动作和人工审批

### 我做了什么

我创建并运行了：

`demos/06-guardrails/demo.py`

这个 demo 定义了一组高风险动作：

- `push_default_branch`
- `merge_pull_request`
- `delete_repository`
- `expose_secret`
- `change_production_config`

这些动作默认不能直接执行，除非传入 `human_approved=True`。

### 我观察到的结果

低风险动作可以直接执行：

```text
已允许：create_feature_branch

高风险动作在没有人工审批时会被阻止：
已阻止：merge_pull_request 需要人工审批。
当传入 human_approved=True 后，同一个高风险动作被允许：
已允许：merge_pull_request
我还测试了生产配置修改：
已阻止：change_production_config 需要人工审批。
我的理解
guardrails 不是为了让 agent 不能工作，而是为了让 agent 在安全边界内工作。
低风险动作可以自动执行，例如读取资料、生成计划、创建 feature branch。
高风险动作必须通过受控路径，例如人工审批、日志记录、权限限制、required checks 或 CODEOWNERS review。
高风险动作包括：
合并 PR
推送默认分支
修改生产配置
删除仓库或资源
暴露 secret
执行不可逆操作
对 GH-600 的意义
这个 demo 对应 GH-600 中的几个考点：
guardrails
human-in-the-loop
autonomy level
accountability
least privilege
auditability
controlled execution path
考试中如果看到 production、default branch、merge、secret、delete、compliance、irreversible 等关键词，应该优先考虑审批、权限限制、日志、回滚和可审计机制。