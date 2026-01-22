# 56. Word Count in List
# Input: ['apple', 'banana', 'apple', 'orange', 'banana']
# Output: {'apple':2, 'banana':2, 'orange':1}

lst = ['apple', 'banana', 'apple', 'orange', 'banana']
d = {}
for word in lst:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
print(d)

