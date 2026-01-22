# 62. Dictionary from List with Counts
# Input: [1,2,2,3,3,3]
# Output: {1:1, 2:2, 3:3}

lst = [1, 2, 2, 3, 3, 3]
d = {}
for num in lst:
    if num in d:
        d[num] += 1
    else:
        d[num] = 1
print(d)

