# 33. Sum of odd-indexed elements
# Input: [1, 2, 3, 4, 5]
# Output: 2 + 4 = 6

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))
    lst.append(ele)

sum_odd_indexed = 0
for i in range(len(lst)):
    if i % 2 != 0:
        sum_odd_indexed += lst[i]

print(f"Sum of odd-indexed elements: {sum_odd_indexed}")

