#Convert uppercase letters to lowercase (without using lower())
word = input("Enter a word in uppercase: ")
lowercase_word = ""
for char in word:
    if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        lowercase_word += chr(ord(char) + 32)
    else:
        lowercase_word += char