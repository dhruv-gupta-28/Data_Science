# 8. Find the smallest digit in a number.

num = int(input("Enter a number: "))
original = num

if num == 0:
    smallest = 0
else:
    smallest = 9
    while num > 0:
        digit = num % 10
        if digit < smallest:
            smallest = digit
        num = num // 10

print(f"Smallest digit in {original} is: {smallest}")

