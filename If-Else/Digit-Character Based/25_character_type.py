# 25. Check if a character is uppercase, lowercase, digit, or special symbol.

char = input("Enter a character: ")

if len(char) == 1:
    if char.isupper():
        print("The character is uppercase.")
    elif char.islower():
        print("The character is lowercase.")
    elif char.isdigit():
        print("The character is a digit.")
    else:
        print("The character is a special symbol.")
else:
    print("Please enter a single character.")