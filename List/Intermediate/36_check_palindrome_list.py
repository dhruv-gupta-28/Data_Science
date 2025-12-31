# 36. Check palindrome list
# Input: [1, 2, 3, 2, 1]
# Output: Palindrome

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))
    lst.append(ele)

# Create reversed list manually
reversed_lst = []
for i in range(len(lst) - 1, -1, -1):
    reversed_lst.append(lst[i])

# Check if palindrome
is_palindrome = True
for i in range(len(lst)):
    if lst[i] != reversed_lst[i]:
        is_palindrome = False
        break

if is_palindrome:
    print("Palindrome")
else:
    print("Not Palindrome")

