#Replace all vowels with *.
str = input("Enter a string: ")
vowels = "aeiouAEIOU"
for char in str:
    if char in vowels:
        str = str.replace(char, '*')
print("String after replacing vowels with *: ", str)