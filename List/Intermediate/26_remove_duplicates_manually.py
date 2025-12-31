# 26. Remove duplicates (manually)
# Input: [1, 2, 2, 3, 4, 4, 5]
# Output: [1, 2, 3, 4, 5]

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))
    lst.append(ele)

unique = []
for element in lst:
    found = False
    for u in unique:
        if u == element:
            found = True
            break
    if not found:
        unique.append(element)

print(f"List without duplicates: {unique}")

