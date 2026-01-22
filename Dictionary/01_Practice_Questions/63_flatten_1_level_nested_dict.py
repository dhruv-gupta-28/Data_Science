# 63. Flatten 1-Level Nested Dictionary
# Input: {'a':1, 'b':{'c':2,'d':3}}
# Output: {'a':1, 'c':2, 'd':3}

d = {'a': 1, 'b': {'c': 2, 'd': 3}}
result = {}
for key, value in d.items():
    if isinstance(value, dict):
        for k, v in value.items():
            result[k] = v
    else:
        result[key] = value
print(result)

