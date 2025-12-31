#Count how many letters, digits, and special characters are in a string.
str = input("Enter a string: ")
letters = 0
digits = 0
special_characters = 0 
for char in str:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
    else:
        special_characters += 1