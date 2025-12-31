# 37. Find frequency of all elements
# Input: [1, 2, 2, 3, 3, 3]
# Output: 1 → 1, 2 → 2, 3 → 3

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))
    lst.append(ele)

# Find unique elements
unique = []
for element in lst:
    found = False
    for u in unique:
        if u == element:
            found = True
            break
    if not found:
        unique.append(element)

# Count frequency
print("Frequency of elements:")
for element in unique:
    count = 0
    for num in lst:
        if num == element:
            count += 1
    print(f"{element} → {count}")

