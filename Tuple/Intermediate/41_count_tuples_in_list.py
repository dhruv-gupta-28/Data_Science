# 41. Count tuples in a list
# Input: [(1,2), (3,4), (5,6)]
# Output: 3

lst = [(1, 2), (3, 4), (5, 6)]

count = 0
for item in lst:
    if type(item) == tuple:
        count += 1

print(count)

