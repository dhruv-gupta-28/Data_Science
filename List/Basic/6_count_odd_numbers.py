# 6. Count odd numbers
# Input: [2, 3, 5, 6, 8]
# Output: 2

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))
    lst.append(ele)

odd_count = 0
for num in lst:
    if num % 2 != 0:
        odd_count += 1

print(f"Count of odd numbers: {odd_count}")

