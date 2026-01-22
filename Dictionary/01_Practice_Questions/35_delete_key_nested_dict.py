# 35. Delete Key from Nested Dictionary
# Input: {'student': {'name': 'Aman', 'age': 17, 'city': 'Delhi'}}
# Delete key "city"
# Output: {'student': {'name': 'Aman', 'age': 17}}

d = {'student': {'name': 'Aman', 'age': 17, 'city': 'Delhi'}}
del d['student']['city']
print(d)

