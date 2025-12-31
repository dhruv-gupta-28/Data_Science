# 19. Check if two numbers differ by less than 10.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

difference = abs(num1 - num2)

if difference < 10:
    print("The numbers differ by less than 10.")
else:
    print("The numbers differ by 10 or more.")