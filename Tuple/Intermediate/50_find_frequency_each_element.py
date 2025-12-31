# 50. Find frequency of each element
# Input: (1, 2, 1, 3, 2, 1)
# Output: {1: 3, 2: 2, 3: 1}

t = (1, 2, 1, 3, 2, 1)

# Get unique elements
unique_list = []
for element in t:
    found = False
    for u in unique_list:
        if u == element:
            found = True
            break
    if not found:
        unique_list.append(element)

# Count frequency
frequency = {}
for element in unique_list:
    count = 0
    for num in t:
        if num == element:
            count += 1
    frequency[element] = count

print(frequency)

