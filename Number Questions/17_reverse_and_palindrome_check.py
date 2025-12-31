# 17. Find the reverse of a number and check if it is equal to original (palindrome check)

num = int(input("Enter a number: "))
original = num
reverse = 0

while num > 0:
    remainder = num % 10
    reverse = reverse * 10 + remainder
    num = num // 10

print(f"Original number: {original}")
print(f"Reversed number: {reverse}")

if original == reverse:
    print(f"{original} is a palindrome.")
else:
    print(f"{original} is not a palindrome.")

