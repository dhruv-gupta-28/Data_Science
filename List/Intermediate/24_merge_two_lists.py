# 24. Merge two lists into one
# Input: [1, 2, 3], [4, 5, 6]
# Output: [1, 2, 3, 4, 5, 6]

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

merged = []
for element in lst1:
    merged.append(element)
for element in lst2:
    merged.append(element)

print(f"Merged list: {merged}")

