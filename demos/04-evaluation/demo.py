EXPECTED = {
    "has_plan": True,
    "has_tests": True,
    "has_rollback": True,
    "uses_allowed_tools_only": True,
}


OUTPUT = {
    "has_plan": True,
    "has_tests": False,
    "has_rollback": True,
    "uses_allowed_tools_only": True,
}


def evaluate(expected: dict, output: dict) -> list[str]:
    failures = []

    for key, required_value in expected.items():
        actual_value = output.get(key)

        if actual_value != required_value:
            failures.append(key)

    return failures


def classify_failure(failure: str) -> str:
    mapping = {
        "has_plan": "推理或计划失败",
        "has_tests": "缺少评估产物",
        "has_rollback": "操作安全失败",
        "uses_allowed_tools_only": "工具误用",
    }

    return mapping.get(failure, "未知原因")


if __name__ == "__main__":
    failures = evaluate(EXPECTED, OUTPUT)

    if not failures:
        print("评估通过：输出满足全部成功标准。")

    for failure in failures:
        print(f"评估失败：{failure} -> {classify_failure(failure)}")