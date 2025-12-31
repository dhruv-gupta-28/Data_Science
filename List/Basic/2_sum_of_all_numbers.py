# 2. Find sum of all numbers
# Input: [4, 2, 6, 1]
# Output: 13

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))
    lst.append(ele)

sum_total = 0
for num in lst:
    sum_total += num

print(f"Sum of all numbers: {sum_total}")

