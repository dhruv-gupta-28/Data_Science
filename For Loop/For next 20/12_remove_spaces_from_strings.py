#Remove all spaces from a string
sentence = input("Enter a sentence: ")
no_space_sentence = ""
for char in sentence:
    if char != ' ':
        no_space_sentence += char
print("Sentence without spaces:", no_space_sentence)