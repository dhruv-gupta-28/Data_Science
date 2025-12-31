# 46. Check if a point (x, y) lies in which quadrant.

x = int(input("Enter the x-coordinate: "))
y = int(input("Enter the y-coordinate: "))

if x > 0 and y > 0:
    print("The point lies in the First Quadrant.")
elif x < 0 and y > 0:
    print("The point lies in the Second Quadrant.")
elif x < 0 and y < 0:
    print("The point lies in the Third Quadrant.")
elif x > 0 and y < 0:
    print("The point lies in the Fourth Quadrant.")
elif x == 0 and y != 0:
    print("The point lies on the Y-axis.")
elif x != 0 and y == 0:
    print("The point lies on the X-axis.")
else: # x == 0 and y == 0
    print("The point is at the origin.")