# 52. Convert List of Dicts Into One Dict
# Input: [{'id':1,'name':'A'}, {'id':2,'name':'B'}]
# Use "id" as key
# Output: {1:'A', 2:'B'}

lst = [{'id': 1, 'name': 'A'}, {'id': 2, 'name': 'B'}]
result = {}
for item in lst:
    result[item['id']] = item['name']
print(result)

