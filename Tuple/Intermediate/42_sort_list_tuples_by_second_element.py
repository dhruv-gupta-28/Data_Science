# 42. Sort a list of tuples by the second element
# Input: [(1, 3), (2, 1), (4, 2)]
# Output: [(2, 1), (4, 2), (1, 3)]

lst = [(1, 3), (2, 1), (4, 2)]

# Selection sort by second element
for i in range(len(lst)):
    min_index = i
    for j in range(i + 1, len(lst)):
        if lst[j][1] < lst[min_index][1]:
            min_index = j
    lst[i], lst[min_index] = lst[min_index], lst[i]

print(lst)

