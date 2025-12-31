# 9. Count even and odd digits in a number.

num = int(input("Enter a number: "))
original = num
even_count = 0
odd_count = 0

while num > 0:
    digit = num % 10
    if digit % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    num = num // 10

print(f"In {original}:")
print(f"Even digits: {even_count}")
print(f"Odd digits: {odd_count}")

