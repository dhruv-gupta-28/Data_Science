# Task 5: Greeting System
# Goal: Based on current time:
# Morning (5–12), Afternoon (12–17), Evening (17–21), Night (21–5)

from datetime import datetime

# Get current time
now = datetime.now()
current_hour = now.hour

# Determine greeting based on hour
if 5 <= current_hour < 12:
    greeting = "Good Morning!"
    period = "Morning (5-12)"
elif 12 <= current_hour < 17:
    greeting = "Good Afternoon!"
    period = "Afternoon (12-17)"
elif 17 <= current_hour < 21:
    greeting = "Good Evening!"
    period = "Evening (17-21)"
else:
    greeting = "Good Night!"
    period = "Night (21-5)"

print(f"Current time: {now.strftime('%H:%M:%S')}")
print(f"Time period: {period}")
print(greeting)
