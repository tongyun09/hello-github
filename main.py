"""hello-github 范例项目主程序。"""

from datetime import date


def greet(name: str = "GitHub") -> str:
    """返回一句问候语。"""
    return f"Hello, {name}! 今天是 {date.today().isoformat()}"


def main() -> None:
    print(greet())
    print("这是我的第一个 GitHub 项目！")
    print("很高兴认识你！")

if __name__ == "__main__":
    main()
