#Find frequency of all elements
n = int(input("Enter number of elements: "))
li = []
for i in range(n):
    ele = int(input(f"Enter element {n}"))
    li.append(ele)
freq = {}
for j in li :
    if j in freq:
        freq[j]= freq[j]+1
    else:
        freq[j]=1
print(freq)