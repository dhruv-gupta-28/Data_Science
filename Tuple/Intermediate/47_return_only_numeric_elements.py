# 47. Return only numeric elements
# Input: (1, "apple", 2.5, True)
# Output: (1, 2.5, True)

t = (1, "apple", 2.5, True)

numeric_list = []
for element in t:
    if isinstance(element, (int, float, bool)):
        numeric_list.append(element)

result = tuple(numeric_list)
print(result)

