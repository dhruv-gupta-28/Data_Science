# 48. Increase Salaries by 15%
# Input: {'Amit': 20000, 'Riya': 30000}
# Output: {'Amit': 23000.0, 'Riya': 34500.0}

d = {'Amit': 20000, 'Riya': 30000}
for key in d:
    d[key] = d[key] * 1.15
print(d)

