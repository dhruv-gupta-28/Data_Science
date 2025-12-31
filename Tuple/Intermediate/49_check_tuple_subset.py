# 49. Check if one tuple is subset of another
# Input: (1, 2) in (1, 2, 3, 4)
# Output: True

t1 = (1, 2)
t2 = (1, 2, 3, 4)

is_subset = True
for element in t1:
    found = False
    for num in t2:
        if num == element:
            found = True
            break
    if not found:
        is_subset = False
        break

print(is_subset)

