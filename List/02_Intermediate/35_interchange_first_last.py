# 35. Interchange first and last element
# Input: [10, 20, 30, 40, 50]
# Output: [50, 20, 30, 40, 10]

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))
    lst.append(ele)

# Interchange first and last
if len(lst) > 0:
    lst[0], lst[-1] = lst[-1], lst[0]

print(f"List after interchanging: {lst}")

