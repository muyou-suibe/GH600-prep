# GH-600 Agentic AI Developer Prep

这个仓库用于系统化准备 GH-600: GitHub Certified Agentic AI Developer 考试。

本仓库重点记录：

- GH-600 官方考试域和技能点
- Agentic AI 与 SDLC 集成相关笔记
- GitHub Copilot、custom agents、MCP server、agent memory、guardrails 等主题
- 实践练习、模拟题、错题和复盘
- 未来开发个人 Codex skill 的素材和结构

## Exam Quick Facts

- Status: Beta（成绩在 beta 结束后约 8 周公布）
- Level: Intermediate
- Duration: 120 minutes
- Passing score: 700
- Language: English only
- 报名方式: Pearson Vue，首次考试 24 小时后可重考

## 角色画像

需要具备在生产级 SDLC 工作流和开发环境中操作、集成、监督和管理 AI agents 的能力：在 SDLC 内运行 agent 工作流、用 GitHub 控件监督自治行为、用扫描和 artifacts 评估调整 agent 输出、配置 custom agents、安全协调多 agent 执行。

备考不仅要能解释概念，还要能回答场景判断题，例如：什么场景适合用 agent？agent 该在哪些步骤被限制？哪些操作必须 human approval？如何评估 agent 输出是否可靠？

## Exam Focus

GH-600 关注在生产级软件开发生命周期中部署、操作、集成和管理 AI agents。

核心关键词：

- Agentic AI
- SDLC workflow
- GitHub as control plane
- GitHub Copilot
- MCP server
- custom agents
- agent memory
- observability
- evaluation
- multi-agent coordination
- guardrails
- accountability

## Official Exam Domains

| Domain | Weight |
|---|---:|
| 1. 准备代理体系结构和 SDLC 进程 | 15-20% |
| 2. 实施工具使用和环境交互 | 20-25% |
| 3. 管理内存、状态和执行 | 10-15% |
| 4. 执行评估、错误分析和优化 | 15-20% |
| 5. 协调多智能体工作流 | 15-20% |
| 6. 实施防护措施和责任 | 10-15% |

## Repository Structure

- `notes/`：按考试域整理的核心笔记（学习阶段）
- `practice/`：错题记录 + 场景实践记录（备考阶段），配套两个可直接使用的 prompt
- `review/`：考后复盘（考后阶段）
- `skill/`：把前三个阶段沉淀出的知识和 prompt，整理成可复用的 Codex skill

## Current Study Rule

每个考试域都要形成三类产出，分别对应仓库的三个阶段：

1. `notes/` 中的概念笔记（学）
2. `practice/scenarios.md` 中的实践记录 + `practice/mistakes.md` 中的错题（练）
3. `review/exam-review.md` 中的复盘结论（复盘）
