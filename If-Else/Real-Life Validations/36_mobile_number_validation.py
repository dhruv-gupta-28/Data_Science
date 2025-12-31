# 36. Check if a mobile number has exactly 10 digits.

mobile_number = input("Enter your mobile number: ")

if len(mobile_number) == 10 and mobile_number.isdigit():
    print("The mobile number is valid.")
else:
    print("The mobile number is invalid. It must have exactly 10 digits.")