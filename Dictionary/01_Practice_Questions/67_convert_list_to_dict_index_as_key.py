# 67. Convert List to Dict Using Index as Key
# Input: ['a','b','c']
# Output: {0:'a', 1:'b', 2:'c'}

lst = ['a', 'b', 'c']
d = {}
for i in range(len(lst)):
    d[i] = lst[i]
print(d)

