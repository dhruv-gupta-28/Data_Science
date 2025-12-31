# 6. Count the number of digits in a number.

num = int(input("Enter a number: "))
original = num
count = 0

if num == 0:
    count = 1
else:
    while num > 0:
        count += 1
        num = num // 10

print(f"Number of digits in {original} is: {count}")

