# 53. Sort Dictionary by Keys
# Input: {'b':2, 'a':1, 'c':3}
# Output: {'a':1, 'b':2, 'c':3}

d = {'b': 2, 'a': 1, 'c': 3}
sorted_keys = sorted(d.keys())
result = {}
for key in sorted_keys:
    result[key] = d[key]
print(result)

