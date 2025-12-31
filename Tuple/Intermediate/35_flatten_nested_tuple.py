# 35. Flatten a nested tuple
# Input: ((1, 2), (3, 4))
# Output: (1, 2, 3, 4)

t = ((1, 2), (3, 4))

flattened_list = []
for sub_tuple in t:
    for element in sub_tuple:
        flattened_list.append(element)

result = tuple(flattened_list)
print(result)

