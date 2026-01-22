# 32. Sum of even-indexed elements
# Input: [1, 2, 3, 4, 5]
# Output: 1 + 3 + 5 = 9

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))
    lst.append(ele)

sum_even_indexed = 0
for i in range(len(lst)):
    if i % 2 == 0:
        sum_even_indexed += lst[i]

print(f"Sum of even-indexed elements: {sum_even_indexed}")

