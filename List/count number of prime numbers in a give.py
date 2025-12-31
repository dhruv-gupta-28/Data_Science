#count number of prime numbers in a given list 
n = int(input("Enter the number of elements in the list: "))
li = []
for i in range(n):
    ele = int(input("Enter element {}: ".format(i+1)))
    li.append(ele)
count = 0
for num in li:
    if num == 2 :
        count += 1
    elif num > 2:
        for i in range(2, num-1):
            if (num % i) == 0:
                break
        else:
            count += 1
print("Number of prime numbers in the list:", count)




#count number of prime numbers in a given list 
n = int(input("Enter the number of elements in the list: "))
li = []
for i in range(n):
    ele = int(input("Enter element {}: ".format(i+1)))
    li.append(ele)
count = 0
for num in li:
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if (num % i) == 0:
                break
        else:
            count += 1
print("Number of prime numbers in the list:", count)