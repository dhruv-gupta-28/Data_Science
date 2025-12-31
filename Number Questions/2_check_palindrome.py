# 2. Check if a number is palindrome
# 121 → Palindrome
# 123 → Not palindrome

num = int(input("Enter a number: "))
original = num
reverse = 0

while num > 0:
    remainder = num % 10
    reverse = reverse * 10 + remainder
    num = num // 10

if original == reverse:
    print(f"{original} is a palindrome.")
else:
    print(f"{original} is not a palindrome.")

