"""hello-github 范例项目主程序。"""

from datetime import date
import json
from pathlib import Path

TASKS_FILE = Path(__file__).parent / "tasks.json"

# 问候函数
def greet(name: str = "GitHub") -> str:
    """返回一句问候语。"""
    return f"Hello, {name}! 今天是 {date.today().isoformat()}"

# 任务读取函数
def load_tasks() -> list:
    """从文件读取任务，文件不存在时返回空列表。"""
    if TASKS_FILE.exists():
        return json.loads(TASKS_FILE.read_text(encoding="utf-8"))
    return []

# 任务保存函数
def save_tasks(tasks: list) -> None:
    """把任务保存到文件。"""
    TASKS_FILE.write_text(
        json.dumps(tasks, ensure_ascii=False, indent=2), encoding="utf-8"
    )

# 主函数
def main() -> None:
    print(greet())
    print("这是我的第一个 GitHub 项目！")
    print("我的名字是tongyun,很高兴认识你！")

    name = input("你叫什么名字？")
    if name:
        print(greet(name))
    else:
        print("没关系，保持神秘也不错！")

# 待办清单函数
def todo() -> None:
    """简易待办清单。"""
    tasks = load_tasks()  # 原来：tasks = []
    while True:
        print("\n--- 待办清单 ---")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print("(a)添加  (d)删除  (q)退出")
        choice = input("选择: ")

        if choice == "q":
            print("再见！")
            save_tasks(tasks)  # 新增：退出前保存任务
            break
        elif choice == "a":
            task = input("输入新任务: ")
            if task:
                tasks.append(task)
                save_tasks(tasks)  # 新增：添加后立即保存
        elif choice == "d":
            num = input("输入任务编号: ")
            if num.isdigit() and 1 <= int(num) <= len(tasks):
                removed = tasks.pop(int(num) - 1)
                save_tasks(tasks)  # 新增：删除后立即保存
                print(f"已删除: {removed}")
    
if __name__ == "__main__":
    main()
    todo()
