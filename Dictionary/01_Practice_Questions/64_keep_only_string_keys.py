# 64. Keep Only String Keys
# Input: {'a':1, 1:'b', 'c':3}
# Output: {'a':1, 'c':3}

d = {'a': 1, 1: 'b', 'c': 3}
result = {}
for key, value in d.items():
    if isinstance(key, str):
        result[key] = value
print(result)

