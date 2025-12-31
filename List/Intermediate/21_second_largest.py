# 21. Find the second largest element
# Input: [3, 8, 1, 9, 7]
# Output: 8

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))
    lst.append(ele)

# Find maximum
maximum = lst[0]
for num in lst:
    if num > maximum:
        maximum = num

# Find second largest
second_largest = None
for num in lst:
    if num != maximum:
        if second_largest is None or num > second_largest:
            second_largest = num

print(f"Second largest element: {second_largest}")

