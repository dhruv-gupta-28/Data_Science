# 41. Sort without using sort() (selection sort)
# Input: [7, 3, 1, 4, 9]
# Output: [1, 3, 4, 7, 9]

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))
    lst.append(ele)

# Selection sort
for i in range(len(lst)):
    min_index = i
    for j in range(i + 1, len(lst)):
        if lst[j] < lst[min_index]:
            min_index = j
    # Swap
    lst[i], lst[min_index] = lst[min_index], lst[i]

print(f"Sorted list: {lst}")

