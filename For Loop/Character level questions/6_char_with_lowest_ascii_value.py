#Find the character with the lowest ASCII value.
str = input("Enter a string: ")
lowest_char = str[0]
for char in str:
    if ord(char) < ord(lowest_char):
        lowest_char = char
print("Character with the lowest ASCII value is:", lowest_char)