# 12. Sum of positive numbers
# Input: [-3, 5, -1, 4, 0]
# Output: 9

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))
    lst.append(ele)

sum_positive = 0
for num in lst:
    if num > 0:
        sum_positive += num

print(f"Sum of positive numbers: {sum_positive}")

