# Mistakes Log

记录所有错题、猜对题、不确定题、薄弱点和易混概念——这些内容合并到这一个文件，用小标题区分，不做无意义的细分。

## 错题表

| Date | Domain | Topic | Question / Scenario | My Answer | Correct Answer | Root Cause | Review Status |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

## Root Cause 分类

- Concept unclear: 概念不清
- Scenario judgment error: 场景判断错误
- Tool permission confused: 工具权限混淆
- MCP concept unclear: MCP 概念不清
- Memory/state confused: 记忆和状态混淆
- Evaluation signal unclear: 评估信号不清
- Guardrail missed: 忽略防护措施
- Multi-agent conflict missed: 忽略多 agent 冲突

## 按 Domain 统计的薄弱点

| Domain | 错题数 | 高频 Root Cause | 是否已回炉对应 notes |
|---|---:|---|---|
| 1. Agent architecture and SDLC | | | |
| 2. Tools, MCP, environment | | | |
| 3. Memory, state, execution | | | |
| 4. Evaluation, error analysis | | | |
| 5. Multi-agent coordination | | | |
| 6. Guardrails and accountability | | | |

## 易混概念对照

| Concept A | Concept B | Difference |
|---|---|---|
| | | |

## 配套 Prompt：错题复盘

把上面的错题表贴给助手，用下面的 prompt 让它帮你分析：

> 你是 GH-600 错题复盘助手。请根据我的错题记录，分析：
> 1. 我最薄弱的 domain
> 2. 高频错误类型（对照 Root Cause 分类）
> 3. 易混概念
> 4. 应该重新学习的官方主题
> 5. 下一周复习计划
>
> 输出要求：直接指出问题，不要只总结表面错误，要分析 root cause，给出可执行的复习动作。
