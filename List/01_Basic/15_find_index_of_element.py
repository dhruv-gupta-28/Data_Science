# 15. Find index of element
# Input: [10, 20, 30, 40], element = 30
# Output: 2

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))
    lst.append(ele)

element = int(input("Enter element to find: "))
index = -1

for i in range(len(lst)):
    if lst[i] == element:
        index = i
        break

if index != -1:
    print(f"Index of {element}: {index}")
else:
    print(f"{element} not found in the list")

