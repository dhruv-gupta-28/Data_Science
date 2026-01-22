# 47. Find duplicate numbers
# Input: [1, 2, 3, 2, 4, 3, 5]
# Output: [2, 3]

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))
    lst.append(ele)

duplicates = []
seen = []

for element in lst:
    # Check if already seen
    already_seen = False
    for s in seen:
        if s == element:
            already_seen = True
            break
    
    if already_seen:
        # Check if already in duplicates
        already_duplicate = False
        for d in duplicates:
            if d == element:
                already_duplicate = True
                break
        if not already_duplicate:
            duplicates.append(element)
    else:
        seen.append(element)

print(f"Duplicate numbers: {duplicates}")

