# 39. Find uncommon elements of two lists
# Input: [1, 2, 3, 4], [3, 4, 5, 6]
# Output: [1, 2, 5, 6]

n1 = int(input("Enter number of elements in first list: "))
lst1 = []
for i in range(n1):
    ele = int(input(f"Enter element {i+1}: "))
    lst1.append(ele)

n2 = int(input("Enter number of elements in second list: "))
lst2 = []
for i in range(n2):
    ele = int(input(f"Enter element {i+1}: "))
    lst2.append(ele)

uncommon = []

# Elements in lst1 but not in lst2
for element in lst1:
    found = False
    for num in lst2:
        if num == element:
            found = True
            break
    if not found:
        uncommon.append(element)

# Elements in lst2 but not in lst1
for element in lst2:
    found = False
    for num in lst1:
        if num == element:
            found = True
            break
    if not found:
        uncommon.append(element)

print(f"Uncommon elements: {uncommon}")

