# 33. Replace an element inside a tuple
# Input: (1, 2, 3, 4) → replace 3 with 99
# Output: (1, 2, 99, 4)

t = (1, 2, 3, 4)
old_value = 3
new_value = 99

result_list = []
for element in t:
    if element == old_value:
        result_list.append(new_value)
    else:
        result_list.append(element)

result = tuple(result_list)
print(result)

