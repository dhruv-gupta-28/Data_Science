#Print only unique characters (characters that appear once).
str = input("Enter a string: ")
unique_chars = ""
for char in str:
    count = 0
    for c in str:
        if char == c:
            count += 1
    if count == 1:
        unique_chars += char
print("Unique characters:", unique_chars)