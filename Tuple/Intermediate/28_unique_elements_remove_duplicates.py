# 28. Get unique elements (remove duplicates)
# Input: (1, 2, 2, 3, 1)
# Output: (1, 2, 3)

t = (1, 2, 2, 3, 1)

unique_list = []
for element in t:
    found = False
    for u in unique_list:
        if u == element:
            found = True
            break
    if not found:
        unique_list.append(element)

unique_tuple = tuple(unique_list)
print(unique_tuple)

