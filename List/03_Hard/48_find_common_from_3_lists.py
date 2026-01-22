# 48. Find common numbers from 3 lists
# Input: [1, 2, 3], [2, 3, 4], [3, 4, 5]
# Output: [3]

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

n3 = int(input("Enter number of elements in third list: "))
lst3 = []
for i in range(n3):
    ele = int(input(f"Enter element {i+1}: "))
    lst3.append(ele)

common = []
for element in lst1:
    # Check if in lst2
    in_lst2 = False
    for num in lst2:
        if num == element:
            in_lst2 = True
            break
    
    if in_lst2:
        # Check if in lst3
        in_lst3 = False
        for num in lst3:
            if num == element:
                in_lst3 = True
                break
        
        if in_lst3:
            # Check if already added
            already_added = False
            for c in common:
                if c == element:
                    already_added = True
                    break
            if not already_added:
                common.append(element)

print(f"Common elements from all three lists: {common}")

