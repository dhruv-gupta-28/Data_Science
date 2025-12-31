#Print ASCII value of each character.
str = input("Enter a string: ")
for char in str:
    print(f"ASCII value of '{char}' is {ord(char)}")