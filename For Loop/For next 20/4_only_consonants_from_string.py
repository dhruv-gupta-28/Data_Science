#Print only consonants from a string
word = input("Enter a word: ")
consonants = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
results = ""
for char in word:
    if char in consonants:
        results += char
print("Consonants in String:", results)