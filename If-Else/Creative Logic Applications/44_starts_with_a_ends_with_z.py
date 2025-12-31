# 44. Check if a string starts with "A" and ends with "Z".

string = input("Enter a string: ").strip()

if string:
    if string[0].upper() == 'A' and string[-1].upper() == 'Z':
        print("The string starts with 'A' and ends with 'Z'.")
    else:
        print("The string does not start with 'A' and end with 'Z'.")
else:
    print("Please enter a valid string.")

