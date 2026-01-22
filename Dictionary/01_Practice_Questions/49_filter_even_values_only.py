# 49. Filter Even Values Only
# Input: {'a': 1, 'b': 2, 'c': 4}
# Output: {'b': 2, 'c': 4}

d = {'a': 1, 'b': 2, 'c': 4}
result = {}
for key, value in d.items():
    if value % 2 == 0:
        result[key] = value
print(result)

