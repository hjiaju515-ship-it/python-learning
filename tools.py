def top_by_key(lst, key_name):
    """从字典列表 lst 里，按 key_name 字段取出该字段最大的那一本字典"""
    return max(lst, key=lambda x: x[key_name])
