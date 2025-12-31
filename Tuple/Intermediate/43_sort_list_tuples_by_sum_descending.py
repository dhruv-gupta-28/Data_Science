# 43. Sort list of tuples by sum of elements (descending)
# Input: [(1, 2), (3, 4), (2, 2)]
# Output: [(3, 4), (2, 2), (1, 2)]

lst = [(1, 2), (3, 4), (2, 2)]

# Selection sort by sum (descending)
for i in range(len(lst)):
    max_index = i
    for j in range(i + 1, len(lst)):
        sum_j = lst[j][0] + lst[j][1]
        sum_max = lst[max_index][0] + lst[max_index][1]
        if sum_j > sum_max:
            max_index = j
    lst[i], lst[max_index] = lst[max_index], lst[i]

print(lst)

