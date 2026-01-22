# 54. Flatten nested list
# Input: [[1, 2], [3, 4], [5, 6]]
# Output: [1, 2, 3, 4, 5, 6]

n = int(input("Enter number of sublists: "))
nested_lst = []
for i in range(n):
    m = int(input(f"Enter number of elements in sublist {i+1}: "))
    sublist = []
    for j in range(m):
        ele = int(input(f"Enter element {j+1}: "))
        sublist.append(ele)
    nested_lst.append(sublist)

flattened = []
for sublist in nested_lst:
    for element in sublist:
        flattened.append(element)

print(f"Flattened list: {flattened}")

