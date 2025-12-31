# 45. Check club entry: age ≥21 and dress code = formal.

age = int(input("Enter your age: "))
dress_code = input("Enter your dress code (formal/casual): ").lower()

if age >= 21:
    if dress_code == "formal":
        print("You are allowed to enter the club.")
    else:
        print("You are not allowed. Dress code must be formal.")
else:
    print("You are not allowed. You must be at least 21 years old.")

