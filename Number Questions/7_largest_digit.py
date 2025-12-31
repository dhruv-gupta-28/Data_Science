# 7. Find the largest digit in a number.

num = int(input("Enter a number: "))
original = num
largest = 0

while num > 0:
    digit = num % 10
    if digit > largest:
        largest = digit
    num = num // 10

print(f"Largest digit in {original} is: {largest}")

