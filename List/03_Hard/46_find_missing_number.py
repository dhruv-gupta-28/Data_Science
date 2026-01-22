# 46. Find missing number in a list (1–n)
# Input: [1, 2, 4, 5]
# Output: 3

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))
    lst.append(ele)

# Find maximum to determine range
maximum = lst[0]
for num in lst:
    if num > maximum:
        maximum = num

# Find missing number
for i in range(1, maximum + 1):
    found = False
    for num in lst:
        if num == i:
            found = True
            break
    if not found:
        print(f"Missing number: {i}")
        break

