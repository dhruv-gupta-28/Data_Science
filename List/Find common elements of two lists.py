#Find common elements of two lists
n = int(input("Enter number of elements"))
li1 = []
li2 = []
li3 = []
for i in range (n):
    ele1 = int(input(f"enetr element {i+1}: "))
    li1.append(ele1)
for i in range (n):
    ele2 = int(input(f"Enter element {i+1}: "))
    li2.append(ele2)
for i in range(n) :
    for j in range (n):
        if li1[i] == li2[j]:
            li3.append(li1[i])
print(li3)