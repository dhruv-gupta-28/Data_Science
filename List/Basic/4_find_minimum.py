# 4. Find minimum element
# Input: [7, 2, 9, 4]
# Output: 2

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))
    lst.append(ele)

minimum = lst[0]
for num in lst:
    if num < minimum:
        minimum = num

print(f"Minimum element: {minimum}")

