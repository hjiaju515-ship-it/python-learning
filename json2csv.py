# import json, csv
#
# # 读 JSON（你已经会的）
# with open("account.json", "r", encoding="utf-8") as f:
#     records = json.load(f)
#
# # 写 CSV
# with open("account.csv", "w", encoding="utf-8", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["type", "amount", "note", "date"])   # 第一行：表头
#     for r in records:
#         writer.writerow([r["type"], r["amount"], r["note"], r["date"]])
x = 40
count = 0
while x > 5:
    x = x - 7
    count += 1
print(count, x)

