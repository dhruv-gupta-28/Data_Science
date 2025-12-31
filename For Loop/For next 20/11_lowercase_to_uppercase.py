#Convert lowercase letters to uppercase (without using upper())
word = input("Enter a word in lowercase: ")
uppercase_word = ""
for char in word:
    if char in 'abcdefghijklmnopqrstuvwxyz':
        uppercase_word += chr(ord(char) - 32)  
    else:
        uppercase_word += char