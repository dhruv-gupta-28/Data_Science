#Sum of odd-indexed elements
n = int(input("Enter number of elements in the list: "))
lst = []
for i in range(n):
    num = int(input("Enter element {}: ".format(i+1)))
    lst.append(num)
sum_odd_indexed = 0
for i in range(1, n, 2):
    sum_odd_indexed += lst[i]
print("Sum of odd-indexed elements in the list:", sum_odd_indexed)