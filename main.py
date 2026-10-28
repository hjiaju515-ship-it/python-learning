# main.py
from mytools.tools import top_by_key     # 包.模块.函数 三层路径

items = [
    {"name": "x", "price": 10, "qty": 3},
    {"name": "y", "price": 5,  "qty": 8},
    {"name": "z", "price": 20, "qty": 1},
]

winner = top_by_key(items, "qty")
print(winner["name"])
