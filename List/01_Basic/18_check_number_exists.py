# 18. Check number exists
# Input: [5, 10, 15, 20], number = 15
# Output: Present

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))
    lst.append(ele)

number = int(input("Enter number to check: "))
found = False

for num in lst:
    if num == number:
        found = True
        break

if found:
    print("Present")
else:
    print("Not Present")

