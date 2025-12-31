# 10. Reverse list manually
# Input: [1, 2, 3, 4]
# Output: [4, 3, 2, 1]

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))
    lst.append(ele)

reversed_lst = []
for i in range(len(lst) - 1, -1, -1):
    reversed_lst.append(lst[i])

print(f"Original list: {lst}")
print(f"Reversed list: {reversed_lst}")

