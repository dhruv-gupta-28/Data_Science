#Count how many special characters are in a string
str = input("Enter a string: ")
special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~\\"
count = 0
for char in str:
    if char in special_characters:
        count += 1
print(f'Number of special characters in the string: {count}')