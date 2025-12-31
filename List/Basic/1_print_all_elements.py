# 1. Print all elements
# Input: [1, 2, 3, 4, 5]
# Output: 1, 2, 3, 4, 5 (each on new line)

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))
    lst.append(ele)

print("Elements of the list:")
for element in lst:
    print(element)

