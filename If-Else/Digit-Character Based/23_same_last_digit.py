# 23. Check if two numbers have the same last digit.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 % 10 == num2 % 10:
    print("The numbers have the same last digit.")
else:
    print("The numbers do not have the same last digit.")