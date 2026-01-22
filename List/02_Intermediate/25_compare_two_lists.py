# 25. Compare two lists (check equality)
# Input: [1, 2, 3], [1, 2, 3]
# Output: Equal

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

if len(lst1) != len(lst2):
    print("Not Equal")
else:
    equal = True
    for i in range(len(lst1)):
        if lst1[i] != lst2[i]:
            equal = False
            break
    
    if equal:
        print("Equal")
    else:
        print("Not Equal")

