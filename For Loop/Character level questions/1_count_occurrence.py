#Count how many times each character appears in a string.
word = input("Enter a string: ")
for char in word:
    count = 0
    for c in word:
        if char == c:
            count += 1
    if word.index(char) == word.index(char):
        print(f"'{char}' occurs {count} times")