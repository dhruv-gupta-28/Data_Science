#Count how many spaces are in a string
sentence = input("Enter a sentence: ")
space_count = 0
for char in sentence:
    if char == ' ':
        space_count += 1
print("Number of spaces in the sentence:", space_count)