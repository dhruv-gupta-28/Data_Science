#Print only vowels from a string
word = input("Enter a string: ")
vowels = "aeiouAEIOU"
result = ""
for char in word:
    if char in vowels:
        result += char
print("Vowels in the string:", result)