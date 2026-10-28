# colorful.py
from colorama import Fore, init
init()                                  # Windows 上启用颜色
from mytools.tools import top_by_key    # 借自己写的包

items = [
    {"name": "x", "price": 10, "qty": 3},
    {"name": "y", "price": 5,  "qty": 8},
    {"name": "z", "price": 20, "qty": 1},
]

winner = top_by_key(items, "qty")
print(Fore.GREEN + "销量冠军: " + winner["name"] + Fore.RESET)
