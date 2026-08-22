"""hello-github 范例项目主程序。"""

from datetime import date
import json
from pathlib import Path

TASKS_FILE = Path(__file__).parent / "tasks.json"


def greet(name: str = "GitHub") -> str:
    """返回一句问候语。"""
    return f"Hello, {name}! 今天是 {date.today().isoformat()}"


def load_tasks() -> list:
    """从文件读取任务，若文件存在则读取，否则返回空列表。兼容旧格式（字符串列表）。"""
    if not TASKS_FILE.exists():
        return []
    data = json.loads(TASKS_FILE.read_text(encoding="utf-8"))
    # 如果读取到的是字符串列表（旧格式），转换为新格式
    if data and isinstance(data[0], str):
        return [{"task": t, "done": False} for t in data]
    return data


def save_tasks(tasks: list) -> None:
    """把任务保存到文件。"""
    TASKS_FILE.write_text(
        json.dumps(tasks, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def main() -> None:
    print(greet())
    print("这是我的第一个 GitHub 项目！")
    print("我的名字是tongyun,很高兴认识你！")

    name = input("你叫什么名字？")
    if name:
        print(greet(name))
    else:
        print("没关系，保持神秘也不错！")


def todo() -> None:
    """简易待办清单（支持完成状态）。"""
    tasks = load_tasks()
    while True:
        print("\n--- 待办清单 ---")
        if not tasks:
            print("（暂无任务）")
        else:
            for i, t in enumerate(tasks, 1):
                status = "✓" if t["done"] else " "
                print(f"{i}. [{status}] {t['task']}")
        print("(a)添加  (d)删除  (t)切换完成状态  (q)退出")
        choice = input("选择: ").strip().lower()

        if choice == "q":
            print("再见！")
            save_tasks(tasks)
            break
        elif choice == "a":
            task = input("输入新任务: ").strip()
            if task:
                tasks.append({"task": task, "done": False})
                save_tasks(tasks)
        elif choice == "d":
            num = input("输入要删除的任务编号: ").strip()
            if num.isdigit() and 1 <= int(num) <= len(tasks):
                removed = tasks.pop(int(num) - 1)
                save_tasks(tasks)
                print(f"已删除: {removed['task']}")
            else:
                print("无效编号")
        elif choice == "t":
            num = input("输入要切换完成状态的任务编号: ").strip()
            if num.isdigit() and 1 <= int(num) <= len(tasks):
                tasks[int(num) - 1]["done"] = not tasks[int(num) - 1]["done"]
                save_tasks(tasks)
            else:
                print("无效编号")
        else:
            print("无效选项，请重新输入")


if __name__ == "__main__":
    main()
    todo()