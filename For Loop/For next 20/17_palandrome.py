#Check if a string is palindrome
str = input("Enter a string: ")
"""
using string method
if str == str[::-1]:
    print(f'"{str}" is a palindrome')
else:
    print(f'"{str}" is not a palindrome')
"""
#using loop
is_palindrome = True
length = len(str)
for i in range(length // 2):
    if str[i] != str[length - i - 1]:
        is_palindrome = False
        break
if is_palindrome:
    print(f'"{str}" is a palindrome')
else:
    print(f'"{str}" is not a palindrome')