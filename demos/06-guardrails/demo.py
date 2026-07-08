RISKY_ACTIONS = {
    "push_default_branch",
    "merge_pull_request",
    "delete_repository",
    "expose_secret",
    "change_production_config",
}


def authorize(action: str, human_approved: bool = False) -> str:
    if action in RISKY_ACTIONS and not human_approved:
        return f"已阻止：{action} 需要人工审批。"

    return f"已允许：{action}"


if __name__ == "__main__":
    print(authorize("create_feature_branch"))
    print(authorize("merge_pull_request"))
    print(authorize("merge_pull_request", human_approved=True))
    print(authorize("change_production_config"))