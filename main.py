"""hello-github 范例项目主程序。"""

from datetime import date


def greet(name: str = "GitHub") -> str:
    """返回一句问候语。"""
    return f"Hello, {name}! 今天是 {date.today().isoformat()}"

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
    """简易待办清单。"""
    tasks = []
    while True:
        print("\n--- 待办清单 ---")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print("(a)添加  (d)删除  (q)退出")
        choice = input("选择: ")

        if choice == "q":
            print("再见！")
            break
        elif choice == "a":
            task = input("输入新任务: ")
            if task:
                tasks.append(task)
        elif choice == "d":
            num = input("输入任务编号: ")
            if num.isdigit() and 1 <= int(num) <= len(tasks):
                removed = tasks.pop(int(num) - 1)
                print(f"已删除: {removed}")
    
if __name__ == "__main__":
    main()
    todo()
