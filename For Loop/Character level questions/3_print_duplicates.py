#Print duplicate characters (characters that appear more than once). withouth using set , string methodscor list 

str = input("Enter a string: ")
duplicates = ""
for i in str:
    count = 0
    for j in str:
        if i == j:
            count += 1
    if count > 1 and i not in duplicates:
        duplicates += i
print("Duplicate characters are:", duplicates)