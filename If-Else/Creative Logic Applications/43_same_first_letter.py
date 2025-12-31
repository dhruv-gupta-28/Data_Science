# 43. Check if two words have the same first letter.

word1 = input("Enter the first word: ").strip()
word2 = input("Enter the second word: ").strip()

if word1 and word2:
    if word1[0].lower() == word2[0].lower():
        print("The two words have the same first letter.")
    else:
        print("The two words do not have the same first letter.")
else:
    print("Please enter valid words.")

