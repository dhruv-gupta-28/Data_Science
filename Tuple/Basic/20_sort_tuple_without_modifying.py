# 20. Sort a tuple without modifying it
# Input: (3, 1, 2)
# Output: (1, 2, 3)

t = (3, 1, 2)

# Convert to list, sort, convert back to tuple
lst = list(t)
# Manual sorting (bubble sort)
for i in range(len(lst)):
    for j in range(len(lst) - 1 - i):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

sorted_tuple = tuple(lst)
print(sorted_tuple)

