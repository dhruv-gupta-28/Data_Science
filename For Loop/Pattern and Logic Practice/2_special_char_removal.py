#Remove all special characters (keep only letters and digits).
str = input("Enter a string: ")
alphabets_digits = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
result = ""
for char in str:
    if char in alphabets_digits:
        result += char
print("String after removing special characters:", result)