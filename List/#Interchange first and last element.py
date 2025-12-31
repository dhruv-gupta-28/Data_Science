#Interchange first and last element
n = int(input("Enter number of elements: "))
li = []
for i in range(n):
    ele = int(input())
    li.append(ele)
print("Original list:", li)
li[0], li[-1] = li[-1], li[0]
print("List after interchanging first and last element:", li)
