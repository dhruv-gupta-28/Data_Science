# 39. Swap Keys and Values
# Input: {'a': 1, 'b': 2}
# Output: {1: 'a', 2: 'b'}

d = {'a': 1, 'b': 2}
swapped = {}
for key, value in d.items():
    swapped[value] = key
print(swapped)

