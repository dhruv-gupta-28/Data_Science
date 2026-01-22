# 3. Find maximum element
# Input: [3, 8, 1, 5]
# Output: 8

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))
    lst.append(ele)

maximum = lst[0]
for num in lst:
    if num > maximum:
        maximum = num

print(f"Maximum element: {maximum}")

