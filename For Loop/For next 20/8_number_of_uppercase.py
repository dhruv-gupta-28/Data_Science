#Count how many uppercase letters are in a string
word = input("Enter a string: ")
count = 0
for letter in word:
    if letter.isupper():
        count += 1
print("Number of uppercase letters:", count)