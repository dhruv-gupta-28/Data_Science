# 7. Find average
# Input: [10, 20, 30, 40]
# Output: 25.0

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))
    lst.append(ele)

sum_total = 0
for num in lst:
    sum_total += num

average = sum_total / len(lst)
print(f"Average: {average}")

