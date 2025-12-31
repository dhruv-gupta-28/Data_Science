#Count how many times the substring "is" appears in a string.
# "This is island" → 2
sentence = input("Enter a sentence: ")
new_sentence = sentence.split()
search = "is"
count = 0
for i in new_sentence:
    if search in i:
        count += 1
print(count)