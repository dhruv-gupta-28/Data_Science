# 40. Find intersection count
# Input: [2, 3, 4], [3, 4, 5, 6]
# Output: 2

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

# Find unique common elements
common = []
for element in lst1:
    # Check if in lst2
    in_lst2 = False
    for num in lst2:
        if num == element:
            in_lst2 = True
            break
    
    if in_lst2:
        # Check if already counted
        already_counted = False
        for c in common:
            if c == element:
                already_counted = True
                break
        if not already_counted:
            common.append(element)

print(f"Intersection count: {len(common)}")

