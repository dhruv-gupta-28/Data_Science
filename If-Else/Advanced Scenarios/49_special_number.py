# 49. Check if a two-digit number is a 'special' number.
# A number is special if the sum of its digits plus the product of its digits equals the number.

num = int(input("Enter a two-digit number: "))

if 10 <= num <= 99:
    digit1 = num // 10
    digit2 = num % 10
    
    sum_of_digits = digit1 + digit2
    product_of_digits = digit1 * digit2
    
    if sum_of_digits + product_of_digits == num:
        print(f"{num} is a special two-digit number.")
    else:
        print(f"{num} is not a special two-digit number.")
else:
    print("Please enter a valid two-digit number.")