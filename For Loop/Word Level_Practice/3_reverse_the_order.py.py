#Reverse the order of words in a sentence.
sentence = input("Enter a sentence: ")
words = sentence.split()
reversed_words = []
for i in range(len(words)-1, -1, -1):
    reversed_words.append(words[i])
reversed_sentence = ' '.join(reversed_words)
print("Reversed sentence:", reversed_sentence)