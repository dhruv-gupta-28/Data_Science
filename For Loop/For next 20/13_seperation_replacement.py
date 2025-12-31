#Replace spaces with a dash (-)
sentence = input("Enter a sentence: ")

# this can be directly done by using replace method but as we hae to use for loop we will use another approach
# modified_sentence = sentence.replace(" ", "-")
modified_sentence = ""
for char in sentence:
    if char == " ":
        modified_sentence += "-"
    else:
        modified_sentence += char
print("Modified sentence:", modified_sentence)