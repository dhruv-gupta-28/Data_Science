# 41. Check if three numbers form a Pythagorean triplet.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

# Sort to find the largest (hypotenuse)
if a > b and a > c:
    hypotenuse = a
    side1 = b
    side2 = c
elif b > a and b > c:
    hypotenuse = b
    side1 = a
    side2 = c
else:
    hypotenuse = c
    side1 = a
    side2 = b

if side1**2 + side2**2 == hypotenuse**2:
    print("The three numbers form a Pythagorean triplet.")
else:
    print("The three numbers do not form a Pythagorean triplet.")

