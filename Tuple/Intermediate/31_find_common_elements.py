# 31. Find common elements between two tuples
# Input: (1, 2, 3) and (2, 3, 4)
# Output: (2, 3)

t1 = (1, 2, 3)
t2 = (2, 3, 4)

common_list = []
for element in t1:
    # Check if in t2
    in_t2 = False
    for num in t2:
        if num == element:
            in_t2 = True
            break
    
    if in_t2:
        # Check if already added
        already_added = False
        for c in common_list:
            if c == element:
                already_added = True
                break
        if not already_added:
            common_list.append(element)

result = tuple(common_list)
print(result)

