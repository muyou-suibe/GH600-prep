AGENTS = {
    "researcher": {
        "说明": "研究型智能体，只能读取资料和搜索仓库",
        "tools": {"read_docs", "search_repo"},
    },
    "editor": {
        "说明": "编辑型智能体，可以读取资料、搜索仓库和修改文件",
        "tools": {"read_docs", "search_repo", "edit_file"},
    },
    "release_manager": {
        "说明": "发布型智能体，可以读取资料和创建 PR，但不能直接修改文件",
        "tools": {"read_docs", "create_pr"},
    },
}


def call_tool(agent: str, tool: str) -> str:
    allowed_tools = AGENTS[agent]["tools"]

    if tool not in allowed_tools:
        return f"已拒绝：{agent} 不能使用工具 {tool}"

    return f"已允许：{agent} 使用工具 {tool}"


if __name__ == "__main__":
    checks = [
        ("researcher", "read_docs"),
        ("researcher", "edit_file"),
        ("editor", "edit_file"),
        ("release_manager", "create_pr"),
        ("release_manager", "edit_file"),
    ]

    for agent, tool in checks:
        print(call_tool(agent, tool))