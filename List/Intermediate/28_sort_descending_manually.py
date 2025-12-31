# 28. Sort descending manually
# Input: [5, 2, 8, 1]
# Output: [8, 5, 2, 1]

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))
    lst.append(ele)

# Selection sort (descending)
for i in range(len(lst)):
    max_index = i
    for j in range(i + 1, len(lst)):
        if lst[j] > lst[max_index]:
            max_index = j
    # Swap
    lst[i], lst[max_index] = lst[max_index], lst[i]

print(f"Sorted list (descending): {lst}")

