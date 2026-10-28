# students = [
#     {"name": "阿珍", "score": 87},
#     {"name": "阿强", "score": 95},
#     {"name": "小红", "score": 78},
#     {"name": "阿明", "score": 92},
# ]
#
# def top_student(sts):
#     return max(sts, key= lambda x:x["score"])
#
# champ = top_student(students)
# print(champ["name"], champ["score"])

# def to_int(text, default):
#     # 试着把 text 转成整数；转不成（ValueError）就返回 default
#     try:
#         return int(text)
#     except ValueError:
#         return default
#
# print(to_int("42", 0))    # 应该是 42
# print(to_int("abc", 0))   # 应该是 ?

def top_by_key(lst,key_name):
    return max(lst,key=lambda x:x[key_name])
items = [
    {"name": "x", "price": 10, "qty": 3},
    {"name": "y", "price": 5,  "qty": 8},
    {"name": "z", "price": 20, "qty": 1},
]
print(top_by_key(items, "qty")["name"])