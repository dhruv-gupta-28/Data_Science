#Swap the case of each character manually
#"HeLLo" → "hEllO"
str = input("Enter a string: ")
swapped_str = ""
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for char in str:
    if char in lowercase:
        index = lowercase.index(char)
        swapped_str += uppercase[index]
    elif char in uppercase:
        index = uppercase.index(char)
        swapped_str += lowercase[index]
    else:
        swapped_str += char
print("Swapped case string:", swapped_str)