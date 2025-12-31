#Count how many lowercase letters are in a string
word = input("Enter a string: ")
count = 0
for char in word:
    if char.islower():
        count += 1
print("Number of lowercase letters:", count)