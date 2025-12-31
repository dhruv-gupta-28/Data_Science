# 22. Find the second smallest element
# Input: [10, 2, 5, 1, 8]
# Output: 2

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))
    lst.append(ele)

# Find minimum
minimum = lst[0]
for num in lst:
    if num < minimum:
        minimum = num

# Find second smallest
second_smallest = None
for num in lst:
    if num != minimum:
        if second_smallest is None or num < second_smallest:
            second_smallest = num

print(f"Second smallest element: {second_smallest}")

