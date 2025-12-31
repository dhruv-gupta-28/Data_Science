# 42. Bubble sort manually
# Input: [5, 1, 4, 2, 8]
# Output: [1, 2, 4, 5, 8]

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))
    lst.append(ele)

# Bubble sort
for i in range(len(lst)):
    for j in range(len(lst) - 1 - i):
        if lst[j] > lst[j + 1]:
            # Swap
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

print(f"Sorted list: {lst}")

