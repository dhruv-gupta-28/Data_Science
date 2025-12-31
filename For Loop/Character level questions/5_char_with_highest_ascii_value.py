#Find the character with the highest ASCII value.
str = input("Enter a string: ")
highest_char = str[0]
for char in str:
    if ord(char) > ord(highest_char):
        highest_char = char
print("Character with the highest ASCII value is:", highest_char)