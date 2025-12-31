# 21. Reverse a tuple
# Input: (1, 2, 3, 4)
# Output: (4, 3, 2, 1)

t = (1, 2, 3, 4)

reversed_list = []
for i in range(len(t) - 1, -1, -1):
    reversed_list.append(t[i])

reversed_tuple = tuple(reversed_list)
print(reversed_tuple)

