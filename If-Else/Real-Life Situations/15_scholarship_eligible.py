# 15. Check if a student qualifies for scholarship (marks >85 and attendance >75%).

marks = float(input("Enter your marks: "))
attendance = float(input("Enter your attendance percentage: "))

if marks > 85:
    if attendance > 75:
        print("You qualify for the scholarship!")
    else:
        print("You do not qualify. Attendance must be above 75%.")
else:
    print("You do not qualify. Marks must be above 85.")