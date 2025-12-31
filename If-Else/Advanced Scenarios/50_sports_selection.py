# 50. Sports selection: Height ≥170 cm AND fitness test = Pass.

height = float(input("Enter your height in cm: "))
fitness_test = input("Enter your fitness test result (Pass/Fail): ").lower()

if height >= 170:
    if fitness_test == "pass":
        print("You are selected for sports.")
    else:
        print("You are not selected. Fitness test must be Pass.")
else:
    print("You are not selected. Height must be ≥170 cm.")

