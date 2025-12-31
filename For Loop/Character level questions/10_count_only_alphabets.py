#Count how many alphabets are in a string (ignore digits and symbols).
string = input("Enter a string: ")
count = 0
alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for char in string:
    if char in alphabets:
        count += 1
print("Number of alphabets in the string:", count)