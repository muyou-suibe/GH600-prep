from dataclasses import dataclass


@dataclass
class AgentTask:
    goal: str
    input_artifacts: list[str]
    expected_output: str
    success_criteria: list[str]
    approved: bool = False


def plan(task: AgentTask) -> dict:
    return {
        "任务目标": task.goal,
        "输入材料": task.input_artifacts,
        "预期输出": task.expected_output,
        "执行步骤": [
            "检查输入材料",
            "输出结构化计划",
            "等待人工审批",
            "审批后再执行",
        ],
        "成功标准": task.success_criteria,
    }


def execute(task: AgentTask) -> str:
    if not task.approved:
        return "已阻止：执行前需要人工审批。"
    return f"已执行：生成 {task.expected_output}"


if __name__ == "__main__":
    task = AgentTask(
        goal="创建部署检查清单",
        input_artifacts=["issue.md", "service.yml"],
        expected_output="deployment-checklist.md",
        success_criteria=["包含回滚方案", "列出负责人", "包含验证步骤"],
    )

    print(plan(task))
    print(execute(task))

    task.approved = True
    print(execute(task))