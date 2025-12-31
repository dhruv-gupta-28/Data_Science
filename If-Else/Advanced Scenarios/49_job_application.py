# 49. Job application: Eligible if qualification = graduate AND age ≤30.

qualification = input("Enter your qualification (graduate/undergraduate): ").lower()
age = int(input("Enter your age: "))

if qualification == "graduate":
    if age <= 30:
        print("You are eligible for the job application.")
    else:
        print("You are not eligible. Age must be ≤30.")
else:
    print("You are not eligible. Qualification must be graduate.")

