# 45. Delete a Subject from Student
# Input: {'s1': {'math': 90, 'science': 88}}
# Delete "science"
# Output: {'s1': {'math': 90}}

d = {'s1': {'math': 90, 'science': 88}}
del d['s1']['science']
print(d)

