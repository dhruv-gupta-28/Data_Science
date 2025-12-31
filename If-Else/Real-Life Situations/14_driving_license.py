# 14. Driving License: Eligible if age ≥18 and eyesight = good.

age = int(input("Enter your age: "))
eyesight = input("Enter your eyesight status (good/poor): ").lower()

if age >= 18:
    if eyesight == "good":
        print("You are eligible for a driving license.")
    else:
        print("You are not eligible. Eyesight must be good.")
else:
    print("You are not eligible. You must be at least 18 years old.")