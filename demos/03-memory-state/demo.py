from datetime import date, timedelta


MEMORY = [
    {
        "scope": "repository",
        "fact": "运行测试使用 pytest。",
        "last_validated": date.today().isoformat(),
    },
    {
        "scope": "repository",
        "fact": "部署仍使用旧的 staging 脚本。",
        "last_validated": (date.today() - timedelta(days=45)).isoformat(),
    },
    {
        "scope": "user",
        "fact": "用户偏好简洁的 Pull Request 摘要。",
        "last_validated": date.today().isoformat(),
    },
]


def is_stale(memory_item: dict) -> bool:
    last_validated = date.fromisoformat(memory_item["last_validated"])
    return date.today() - last_validated > timedelta(days=28)


def explain(memory_item: dict) -> str:
    status = "已过期" if is_stale(memory_item) else "有效"
    return f"{status}: [{memory_item['scope']}] {memory_item['fact']}"


if __name__ == "__main__":
    for item in MEMORY:
        print(explain(item))