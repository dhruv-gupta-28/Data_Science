# 31. Remove Last Inserted Item
# Input: {'a': 1, 'b': 2, 'c': 3}
# Output: ('c', 3), Remaining: {'a': 1, 'b': 2}

d = {'a': 1, 'b': 2, 'c': 3}
last_key = list(d.keys())[-1]
removed = (last_key, d.pop(last_key))
print(removed)
print(f"Remaining: {d}")

