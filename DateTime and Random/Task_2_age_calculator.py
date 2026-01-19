# Task 2: Age Calculator
# Goal: Ask user for date of birth and calculate:
# - Current age in years
# - Total days lived

from datetime import datetime

# Get date of birth from user
dob_str = input("Enter your date of birth (YYYY-MM-DD): ")
dob = datetime.strptime(dob_str, "%Y-%m-%d")

# Get current date
today = datetime.now()

# Calculate age in years
age_years = today.year - dob.year
if today.month < dob.month or (today.month == dob.month and today.day < dob.day):
    age_years -= 1

# Calculate total days lived
days_lived = (today - dob).days

print(f"Current age in years: {age_years}")
print(f"Total days lived: {days_lived}")
