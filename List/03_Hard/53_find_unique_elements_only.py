# 53. Find unique elements only
# Input: [1, 2, 2, 3, 4, 4, 5]
# Output: [1, 3, 5]

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))
    lst.append(ele)

unique = []
for element in lst:
    count = 0
    for num in lst:
        if num == element:
            count += 1
    if count == 1:
        unique.append(element)

print(f"Unique elements (appearing only once): {unique}")

