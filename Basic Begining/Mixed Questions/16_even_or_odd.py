# 16. Write a program to take a number as input and check if it's even or odd.

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")