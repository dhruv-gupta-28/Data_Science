# 11. Count occurrences
# Input: [2, 4, 2, 6, 2], element = 2
# Output: 3

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))
    lst.append(ele)

element = int(input("Enter element to count: "))
count = 0

for num in lst:
    if num == element:
        count += 1

print(f"Occurrences of {element}: {count}")

