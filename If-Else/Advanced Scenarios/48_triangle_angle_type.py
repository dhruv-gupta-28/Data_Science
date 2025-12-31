# 48. Check the type of triangle based on angles (acute, obtuse, right-angled).

angle1 = int(input("Enter the first angle: "))
angle2 = int(input("Enter the second angle: "))
angle3 = int(input("Enter the third angle: "))

if angle1 + angle2 + angle3 == 180 and angle1 > 0 and angle2 > 0 and angle3 > 0:
    if angle1 == 90 or angle2 == 90 or angle3 == 90:
        print("It is a right-angled triangle.")
    elif angle1 > 90 or angle2 > 90 or angle3 > 90:
        print("It is an obtuse-angled triangle.")
    else:
        print("It is an acute-angled triangle.")
else:
    print("The angles do not form a valid triangle.")