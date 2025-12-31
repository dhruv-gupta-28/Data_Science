# 55. Find Key with Minimum Value
# Input: {'a':5, 'b':1, 'c':3}
# Output: b

d = {'a': 5, 'b': 1, 'c': 3}
min_value = min(d.values())
for key, value in d.items():
    if value == min_value:
        print(key)
        break

