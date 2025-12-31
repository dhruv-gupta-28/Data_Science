# 8. Assign grades based on marks: A (90+), B (75–89), C (50–74), Fail (<50).

marks = float(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
else:
    if marks >= 75:
        print("Grade: B")
    else:
        if marks >= 50:
            print("Grade: C")
        else:
            print("Grade: Fail")