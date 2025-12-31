# 11. Merge Two Dictionaries
# Problem: Merge dict2 into dict1 using update().
# Input: dict1 = {'a': 1, 'b': 2}, dict2 = {'c': 3, 'd': 4}
# Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict1.update(dict2)
print(dict1)

