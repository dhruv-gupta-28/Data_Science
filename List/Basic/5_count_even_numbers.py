# 5. Count even numbers
# Input: [1, 2, 3, 4, 5, 6]
# Output: 3

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))
    lst.append(ele)

even_count = 0
for num in lst:
    if num % 2 == 0:
        even_count += 1

print(f"Count of even numbers: {even_count}")

