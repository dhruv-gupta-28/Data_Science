# 50. Determine the nature of roots of a quadratic equation.

import cmath

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

discriminant = (b**2) - (4*a*c)

if discriminant > 0:
    root1 = (-b - discriminant**0.5) / (2*a)
    root2 = (-b + discriminant**0.5) / (2*a)
    print(f"The roots are real and distinct: {root1} and {root2}")
elif discriminant == 0:
    root1 = root2 = -b / (2*a)
    print(f"The roots are real and equal: {root1}")
else:
    root1 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    root2 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    print(f"The roots are complex and different: {root1} and {root2}")