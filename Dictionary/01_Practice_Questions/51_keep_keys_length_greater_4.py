# 51. Keep Only Keys Length > 4
# Input: {'apple':1, 'bat':2, 'catfish':3}
# Output: {'apple':1, 'catfish':3}

d = {'apple': 1, 'bat': 2, 'catfish': 3}
result = {}
for key, value in d.items():
    if len(key) > 4:
        result[key] = value
print(result)

