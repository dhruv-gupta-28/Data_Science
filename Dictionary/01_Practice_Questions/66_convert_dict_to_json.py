# 66. Convert Dictionary to JSON
# Input: {'name':'Amit', 'age':20}
# Output: {"name": "Amit", "age": 20}

import json
d = {'name': 'Amit', 'age': 20}
json_str = json.dumps(d)
print(json_str)

