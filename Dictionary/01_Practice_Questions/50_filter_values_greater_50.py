# 50. Filter Values > 50
# Input: {'a':30, 'b':60, 'c':90}
# Output: {'b':60, 'c':90}

d = {'a': 30, 'b': 60, 'c': 90}
result = {}
for key, value in d.items():
    if value > 50:
        result[key] = value
print(result)

