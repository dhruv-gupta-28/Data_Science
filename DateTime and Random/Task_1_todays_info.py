# Task 1: Today's Info Program (Beginner)
# Goal: Print Today's date, Current time, Day name (Monday, Tuesday…)

from datetime import datetime

# Get current date and time
now = datetime.now()

# Today's date
today_date = now.strftime("%Y-%m-%d")
print(f"Today's date: {today_date}")

# Current time
current_time = now.strftime("%H:%M:%S")
print(f"Current time: {current_time}")

# Day name
day_name = now.strftime("%A")
print(f"Day name: {day_name}")
