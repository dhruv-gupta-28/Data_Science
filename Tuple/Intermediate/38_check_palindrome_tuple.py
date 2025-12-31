# 38. Check if a tuple is a palindrome
# Input: (1, 2, 3, 2, 1)
# Output: Palindrome

t = (1, 2, 3, 2, 1)

# Create reversed tuple
reversed_list = []
for i in range(len(t) - 1, -1, -1):
    reversed_list.append(t[i])
reversed_t = tuple(reversed_list)

# Check if palindrome
is_palindrome = True
for i in range(len(t)):
    if t[i] != reversed_t[i]:
        is_palindrome = False
        break

if is_palindrome:
    print("Palindrome")
else:
    print("Not Palindrome")

