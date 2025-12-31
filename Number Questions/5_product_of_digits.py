# 5. Find the product of digits of a number.

num = int(input("Enter a number: "))
original = num
product = 1

while num > 0:
    digit = num % 10
    product *= digit
    num = num // 10

print(f"Product of digits of {original} is: {product}")

