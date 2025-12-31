# 13. Multiply all numbers
# Input: [2, 3, 4]
# Output: 24

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))
    lst.append(ele)

product = 1
for num in lst:
    product *= num

print(f"Product of all numbers: {product}")

