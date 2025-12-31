# 37. Convert Two Lists to Dictionary
# Input: keys = ['a','b','c'], values = [1,2,3]
# Output: {'a':1,'b':2,'c':3}

keys = ['a', 'b', 'c']
values = [1, 2, 3]
d = {}
for i in range(len(keys)):
    d[keys[i]] = values[i]
print(d)

