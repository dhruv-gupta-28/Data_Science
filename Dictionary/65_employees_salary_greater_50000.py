# 65. Employees With Salary > 50000
# Input: {'Amit':45000, 'Riya':60000, 'Rahul':52000}
# Output: {'Riya':60000, 'Rahul':52000}

d = {'Amit': 45000, 'Riya': 60000, 'Rahul': 52000}
result = {}
for key, value in d.items():
    if value > 50000:
        result[key] = value
print(result)

