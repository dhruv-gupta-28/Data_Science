# 44. Merge two tuples element-wise
# Input: (1, 2, 3) and (4, 5, 6)
# Output: [(1,4), (2,5), (3,6)]

t1 = (1, 2, 3)
t2 = (4, 5, 6)

result_list = []
for i in range(len(t1)):
    result_list.append((t1[i], t2[i]))

print(result_list)

