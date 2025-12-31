# 37. Check if a date (day, month) is valid.

day = int(input("Enter the day: "))
month = int(input("Enter the month: "))

if month in [1, 3, 5, 7, 8, 10, 12]:
    if 1 <= day <= 31:
        print("The date is valid.")
    else:
        print("The date is invalid.")
elif month in [4, 6, 9, 11]:
    if 1 <= day <= 30:
        print("The date is valid.")
    else:
        print("The date is invalid.")
elif month == 2:
    if 1 <= day <= 29:  # Assuming leap year for simplicity
        print("The date is valid.")
    else:
        print("The date is invalid.")
else:
    print("The date is invalid.")