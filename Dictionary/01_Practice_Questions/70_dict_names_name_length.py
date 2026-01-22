# 70. Dictionary of Names and Name Length
# Input: ['Amit','Riya','Rahul']
# Output: {'Amit':4, 'Riya':4, 'Rahul':5}

names = ['Amit', 'Riya', 'Rahul']
d = {}
for name in names:
    d[name] = len(name)
print(d)

