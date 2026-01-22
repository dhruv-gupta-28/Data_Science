#Check palindrome list
n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    ele = int(input())
    lst.append(ele)
if lst == lst[::-1]:
    print("The list is a palindrome")
else:
    print("The list is not a palindrome")