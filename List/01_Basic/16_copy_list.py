# 16. Copy one list into another
# Input: [1, 2, 3]
# Output: [1, 2, 3]

n = int(input("Enter number of elements: "))
original_lst = []
for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))
    original_lst.append(ele)

copied_lst = []
for element in original_lst:
    copied_lst.append(element)

print(f"Original list: {original_lst}")
print(f"Copied list: {copied_lst}")

