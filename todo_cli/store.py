import json

def read_todo():
    try:
        with open("todo.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_todo(items):
    with open("todo.json", "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)

def add_todo(x):
    items = read_todo()
    items.append({
        "text": x,
        "done": False
    })
    save_todo(items)

def show_todo():
    items = read_todo()
    if len(items) == 0:
        print("还没添加记录哦~")
        return
    count = 0
    for item in items:
        count += 1
        if not item["done"]:
            status = "[ ]"
        else:
            status = "[√]"
        print(f"{count}. {status} {item['text']}")

def done_todo():
    show_todo()
    try:
        n = int(input("输入要完成的记录编号:"))
    except ValueError:
        print("请输入数字")
        return
    items = read_todo()
    if n in range(1, len(items) + 1):
        items[n - 1]["done"] = True
        save_todo(items)
        print("已标记完成")
    else:
        print("没有这条记录哦~")

def remove_todo():
    show_todo()
    try:
        n = int(input("输入要删除的记录编号:"))
    except ValueError:
        print("请输入数字")
        return
    items = read_todo()
    if n in range(1, len(items) + 1):
        items.remove(items[n - 1])
        save_todo(items)
        print("已删除")
    else:
        print("没有这条记录哦~")
