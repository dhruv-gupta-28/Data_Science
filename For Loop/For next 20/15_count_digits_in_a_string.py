#Count how many digits (0–9) are in a string
str =input("Enter a string: ")
count = 0

#with using string methids but we need to do it without using string methods
#for char in str:
#    if char.isdigit():
#        count += 1

for char in str:
    if char in '0123456789':
        count += 1
print("Number of digits in the string:", count)