# 47. Exam eligibility: Allowed if marks ≥40 OR attendance ≥75%.

marks = float(input("Enter your marks: "))
attendance = float(input("Enter your attendance percentage: "))

if marks >= 40 or attendance >= 75:
    print("You are eligible to appear for the exam.")
else:
    print("You are not eligible. You need marks ≥40 OR attendance ≥75%.")

