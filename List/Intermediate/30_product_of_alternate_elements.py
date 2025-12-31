# 30. Product of alternate elements
# Input: [2, 3, 4, 5, 6]
# Output: 2 * 4 * 6 = 48

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))
    lst.append(ele)

product_alternate = 1
for i in range(0, len(lst), 2):
    product_alternate *= lst[i]

print(f"Product of alternate elements: {product_alternate}")

