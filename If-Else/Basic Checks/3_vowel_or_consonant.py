# 3. Check if a character is vowel or consonant.

char = input("Enter a character: ").lower()

if len(char) == 1 and char.isalpha():
    if char in 'aeiou':
        print("The character is a vowel.")
    else:
        print("The character is a consonant.")
else:
    print("Please enter a valid single alphabetic character.")