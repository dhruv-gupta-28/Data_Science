# 24. Check if a number is a palindrome (like 121, 1441).

num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    reverse = reverse * 10 + num % 10
    num //= 10

if original == reverse:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")