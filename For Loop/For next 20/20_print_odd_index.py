#Print characters at odd index positions only
word = input("Enter a word: ")
for i in range(1, len(word), 2):
    print(word[i])