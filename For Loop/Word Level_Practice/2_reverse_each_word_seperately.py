#Reverse each word in a sentence separately.
sentence = input("Enter a sentence: ")
words = sentence.split()
reversed_words = []
for word in words:
    reversed_word = word[::-1]
    reversed_words.append(reversed_word)
reversed_sentence = ' '.join(reversed_words)
print("Reversed sentence:", reversed_sentence)