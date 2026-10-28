# import json
#
# # ① 读
# with open("account.json", "r", encoding="utf-8") as f:
#     records = json.load(f)
#
# # ② 加一笔（纯粹的 append，和 s1c1 一个动作）
# records.append({
#     "type": "支出",
#     "amount": 25.0,
#     "note": "午饭",
#     "date": "2026-10-26"
# })
#
# # ③ 写回
# with open("account.json", "w", encoding="utf-8") as f:
#     json.dump(records, f, ensure_ascii=False, indent=2)
#
#
import json

with open("account.json", "r", encoding="utf-8") as f:
    records = json.load(f)

total_in = 0    # 总收入
total_out = 0   # 总支出

for r in records:
    # 判断这条是收入还是支出，分别累加（你来填）
    if r["type"] == "收入":
        total_in += r["amount"]
    elif r["type"] == "支出":
        total_out += r["amount"]

print("总收入:", total_in)
print("总支出:", total_out)
print("结余:", total_in - total_out)

