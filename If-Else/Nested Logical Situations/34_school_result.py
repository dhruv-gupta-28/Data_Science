# 34. School Result: Pass only if marks ≥33 in all subjects.

subject1 = float(input("Enter marks for subject 1: "))
subject2 = float(input("Enter marks for subject 2: "))
subject3 = float(input("Enter marks for subject 3: "))

if subject1 >= 33 and subject2 >= 33 and subject3 >= 33:
    print("Pass")
else:
    print("Fail")