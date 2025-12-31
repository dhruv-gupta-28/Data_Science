# 40. Check if an entered pin code is 6 digits long.

pin_code = input("Enter your pin code: ")

if len(pin_code) == 6 and pin_code.isdigit():
    print("The pin code is valid.")
else:
    print("The pin code is invalid. It must be 6 digits long.")