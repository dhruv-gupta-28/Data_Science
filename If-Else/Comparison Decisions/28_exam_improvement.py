# 28. Given two exam scores, check if the student improved in the second one.

score1 = float(input("Enter the first exam score: "))
score2 = float(input("Enter the second exam score: "))

if score2 > score1:
    print("The student improved in the second exam.")
elif score2 == score1:
    print("The student scored the same in both exams.")
else:
    print("The student did not improve in the second exam.")