#Count how many words start with a vowel
sentence = input("Enter a sentence: ")
words = sentence.split()
vowel_count = 0
vowels = 'aeiouAEIOU'
for word in words:
    if word[0] in vowels:
        vowel_count += 1
print("Number of words starting with a vowel:", vowel_count)
