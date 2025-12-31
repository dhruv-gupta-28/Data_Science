# 49. Rotate list by n positions (right)
# Input: [1, 2, 3, 4, 5], n = 2
# Output: [4, 5, 1, 2, 3]

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))
    lst.append(ele)

rotate_by = int(input("Enter number of positions to rotate right: "))

# Normalize rotation
rotate_by = rotate_by % len(lst)

# Rotate right
for _ in range(rotate_by):
    # Move last element to front
    last = lst[-1]
    for i in range(len(lst) - 1, 0, -1):
        lst[i] = lst[i - 1]
    lst[0] = last

print(f"List after right rotation by {rotate_by}: {lst}")

