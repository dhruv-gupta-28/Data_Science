# Task 3: Days Left for Exam
# Goal: User enters an exam date → show:
# - Days remaining
# - Whether exam date is past or future

from datetime import datetime

# Get exam date from user
exam_date_str = input("Enter exam date (YYYY-MM-DD): ")
exam_date = datetime.strptime(exam_date_str, "%Y-%m-%d")

# Get current date
today = datetime.now()

# Calculate days difference
days_difference = (exam_date - today).days

if days_difference > 0:
    print(f"Days remaining: {days_difference}")
    print("Exam date is in the future.")
elif days_difference < 0:
    print(f"Days passed: {abs(days_difference)}")
    print("Exam date is in the past.")
else:
    print("Exam is today!")
