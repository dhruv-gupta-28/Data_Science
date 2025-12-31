#Find the shortest word in a sentence.
sentence = input("Enter a sentence: ")
words = sentence.split()
shortest_word = words[0]
for word in words:
    if len(word) < len(shortest_word):
        shortest_word = word
print("The shortest word is:", shortest_word)