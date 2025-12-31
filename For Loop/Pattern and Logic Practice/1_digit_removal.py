#Remove all digits from a string.
# "py123thon" → "python"

str = input("Enter a string: ")
result = ""
digits = "0123456789"
for char in str:
    if char not in digits:
        result += char
print("String after removing digits:", result)