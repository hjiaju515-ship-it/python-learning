import store

while True:
    print("""
====== Todo CLI ======
1. 添加任务
2. 查看任务
3. 标记完成
4. 删除任务
5.退出
    """)
    choice = input("请选择:")

    if choice == "1":
        text = input("输入任务:")
        store.add_todo(text)
        print("已添加!")
        continue
    elif choice == "2":
        store.show_todo()
        continue
    elif choice == "3":
        store.done_todo()
        continue
    elif choice == "4":
        store.remove_todo()
        continue
    elif choice == "5":
        break
    else:
        print("请输入1-5")
        continue