# 20. Check if an entered time is AM or PM.

time = input("Enter time in 24-hour format (HH:MM): ")

hour = int(time.split(':')[0])

if 0 <= hour < 12:
    print("AM")
elif 12 <= hour < 24:
    print("PM")
else:
    print("Invalid time format.")