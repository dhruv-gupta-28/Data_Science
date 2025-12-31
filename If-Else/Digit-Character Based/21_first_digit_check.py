# 21. Check if the first digit of a number is even or odd.

num = int(input("Enter a number: "))

first_digit = int(str(abs(num))[0])

if first_digit % 2 == 0:
    print("The first digit is even.")
else:
    print("The first digit is odd.")