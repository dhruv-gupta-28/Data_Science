# 10. Check whether a triangle is Equilateral, Isosceles, or Scalene.

side1 = float(input("Enter the first side of the triangle: "))
side2 = float(input("Enter the second side of the triangle: "))
side3 = float(input("Enter the third side of the triangle: "))

if side1 == side2:
    if side2 == side3:
        print("The triangle is Equilateral.")
    else:
        print("The triangle is Isosceles.")
else:
    if side2 == side3:
        print("The triangle is Isosceles.")
    else:
        if side1 == side3:
            print("The triangle is Isosceles.")
        else:
            print("The triangle is Scalene.")