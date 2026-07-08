AGENTS = {
    "frontend_agent": {
        "职责": "负责前端页面和模板",
        "files": {"app.py", "templates/index.html"},
    },
    "docs_agent": {
        "职责": "负责文档和安装说明",
        "files": {"README.md", "docs/setup.md"},
    },
    "security_agent": {
        "职责": "负责安全检查和依赖风险",
        "files": {"app.py", "requirements.txt"},
    },
}


def detect_conflicts(agent_map: dict) -> list[str]:
    file_owner = {}
    conflicts = []

    for agent_name, agent_info in agent_map.items():
        for file_path in agent_info["files"]:
            if file_path in file_owner:
                previous_owner = file_owner[file_path]
                conflicts.append(
                    f"{file_path}: {previous_owner} 与 {agent_name} 存在修改冲突"
                )

            file_owner[file_path] = agent_name

    return conflicts


if __name__ == "__main__":
    conflicts = detect_conflicts(AGENTS)

    if not conflicts:
        print("未发现冲突。")

    for conflict in conflicts:
        print(f"发现冲突：{conflict}")