# Domain 4: Evaluation, Error Analysis, and Optimization

权重：15-20%

## 核心问题

如何定义 agent 成功条件，使用日志、计划、trace、输出和 workflow artifacts 分析失败，并根据结果优化 agent 行为。

## 必须掌握

- expected outcomes
- operational constraints
- qualitative evaluation signals
- quantitative evaluation signals
- automatic scanning tools
- logs
- plans
- traces
- outputs
- workflow artifacts
- reasoning errors
- tool misuse
- context issues
- environment issues
- instruction optimization
- workflow optimization
- constraint optimization
- memory optimization
- tool access optimization

## 复习问题

- 如何区分 reasoning error 和 tool misuse？
- workflow artifacts 如何帮助评估 agent 输出？
- 优化 agent 行为时，应该优先改 instructions、tools 还是 constraints？

## Demo 验证：评估、错误分析和优化

### 我做了什么

我创建并运行了：

`demos/04-evaluation/demo.py`

这个 demo 用 `EXPECTED` 表示预期成功标准，用 `OUTPUT` 表示 agent 实际输出。

预期标准包括：

- 有计划
- 有测试
- 有回滚方案
- 只使用允许的工具

### 我观察到的结果

初始版本中，`EXPECTED` 要求：

```python
"has_tests": True

但 OUTPUT 中是：
"has_tests": False
所以程序输出：
评估失败：has_tests -> 缺少评估产物
当我临时把 has_tests 改成 True 后，输出变成：
评估通过：输出满足全部成功标准。
恢复为 False 后，又重新输出失败原因。
我的理解
评估 agent 输出时，不能只看它有没有产出内容，而要看它是否满足预先定义的成功标准。
如果输出不满足标准，需要进一步分类失败原因，例如：
推理或计划失败
缺少评估产物
操作安全失败
工具误用
这样后续才能知道应该优化 prompt、工具权限、工作流、测试流程，还是审批机制。
对 GH-600 的意义
这个 demo 对应 GH-600 中的几个考点：
evaluation signals
error analysis
root cause classification
workflow artifacts
optimization
考试中如果遇到 agent 输出不完整的场景，应该优先考虑：
是否提前定义了成功标准
是否有测试、日志、扫描、PR、计划等可审查产物
失败原因属于推理问题、工具问题、上下文问题，还是环境问题
后续应该通过修改说明、调整工具权限、增加评估信号或加入人工审批来优化