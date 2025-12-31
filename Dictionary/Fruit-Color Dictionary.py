#Fruit-Color Dictionary
dict1 = {}
n = int(input("Enter number of fruits: "))
for i in range(n):
    fruit = input("Enter fruit name: ")
    color = input("Enter fruit color: ")
    dict1[fruit] = color
print("Fruit-Color Dictionary:", dict1)