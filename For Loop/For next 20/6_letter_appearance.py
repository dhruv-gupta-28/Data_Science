#Count how many times a specific character appears
word = input("Enter a word: ")
letter = input("Enter a letter to search for: ")
count = 0
for char in word:
    if char == letter:
        count += 1
print(f"The letter '{letter}' appears {count} times in the word '{word}'.")