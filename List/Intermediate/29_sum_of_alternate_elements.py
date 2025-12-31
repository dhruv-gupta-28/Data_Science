# 29. Sum of alternate elements
# Input: [1, 2, 3, 4, 5, 6]
# Output: 1 + 3 + 5 = 9

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))
    lst.append(ele)

sum_alternate = 0
for i in range(0, len(lst), 2):
    sum_alternate += lst[i]

print(f"Sum of alternate elements: {sum_alternate}")

