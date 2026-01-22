# 45. Merge and sort two lists
# Input: [3, 1, 4], [2, 5, 0]
# Output: [0, 1, 2, 3, 4, 5]

n1 = int(input("Enter number of elements in first list: "))
lst1 = []
for i in range(n1):
    ele = int(input(f"Enter element {i+1}: "))
    lst1.append(ele)

n2 = int(input("Enter number of elements in second list: "))
lst2 = []
for i in range(n2):
    ele = int(input(f"Enter element {i+1}: "))
    lst2.append(ele)

# Merge
merged = []
for element in lst1:
    merged.append(element)
for element in lst2:
    merged.append(element)

# Sort using selection sort
for i in range(len(merged)):
    min_index = i
    for j in range(i + 1, len(merged)):
        if merged[j] < merged[min_index]:
            min_index = j
    merged[i], merged[min_index] = merged[min_index], merged[i]

print(f"Merged and sorted list: {merged}")

