# 32. Find elements present in first tuple but not in second
# Input: (1, 2, 3, 4) and (3, 4, 5)
# Output: (1, 2)

t1 = (1, 2, 3, 4)
t2 = (3, 4, 5)

diff_list = []
for element in t1:
    found = False
    for num in t2:
        if num == element:
            found = True
            break
    if not found:
        diff_list.append(element)

result = tuple(diff_list)
print(result)

