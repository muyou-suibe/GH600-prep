# Scenario Practice

动手实践记录和自测出题，按时间顺序记录在同一个文件里。

## 实践记录

| Date | Domain | 实践内容 | 结论 / 卡住的点 | 是否已写入 notes |
|---|---|---|---|---|
| | | | | |

实践内容建议覆盖：

- 配置 custom instructions
- 研究 custom agents
- 了解并配置 MCP server（remote MCP server、MCP registry、MCP allowlist）
- 配置 Copilot setup steps
- 设计并跑通至少一个 agent workflow 场景（例如：agent 自主创建分支和 PR 时的权限与审批设计）

## 配套 Prompt：场景出题

用下面的 prompt 生成考试风格练习题，检验某个 domain 是否学扎实：

> 你是 GH-600 备考教练。请基于指定 domain 生成考试风格练习题。
> 要求：使用中文出题，保留关键英文术语；题目偏场景判断，不要只考定义；每题给出正确答案和解释；解释为什么其他选项不合适；标注对应 domain 和知识点。
>
> 输入：Domain / Topic / Difficulty / Number of questions
