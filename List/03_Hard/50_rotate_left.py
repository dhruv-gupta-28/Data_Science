# 50. Rotate list by n positions (left)
# Input: [1, 2, 3, 4, 5], n = 2
# Output: [3, 4, 5, 1, 2]

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))
    lst.append(ele)

rotate_by = int(input("Enter number of positions to rotate left: "))

# Normalize rotation
rotate_by = rotate_by % len(lst)

# Rotate left
for _ in range(rotate_by):
    # Move first element to end
    first = lst[0]
    for i in range(len(lst) - 1):
        lst[i] = lst[i + 1]
    lst[-1] = first

print(f"List after left rotation by {rotate_by}: {lst}")

