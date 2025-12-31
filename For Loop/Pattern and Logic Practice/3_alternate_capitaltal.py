#Create a new string with characters at even index in uppercase and odd index in lowercase.
# "python" → "PyThOn"
str = input("Enter a string: ")
new_str = ""
for i in range(len(str)):
    if i % 2 == 0:
        new_str += str[i].upper()
    else:
        new_str += str[i].lower()