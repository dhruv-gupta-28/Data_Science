#Print characters at even index positions only
word = input("Enter a word: ")
for i in range(0, len(word), 2):
    print(word[i])