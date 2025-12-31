#Find the first vowel in a string and print it
str1 = input("Enter a string: ")
vowels = 'aeiouAEIOU'
for char in str1:
    if char in vowels:
        print("The first vowel in the string is:", char)
        break
    