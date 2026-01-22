# 59. Compare Dicts & Return Keys That Differ
# Input: {'a':1, 'b':2}, {'a':1, 'b':3}
# Output: ['b']

d1 = {'a': 1, 'b': 2}
d2 = {'a': 1, 'b': 3}
differing = []
for key in d1:
    if key in d2 and d1[key] != d2[key]:
        differing.append(key)
print(differing)

