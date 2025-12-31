#Sum of even-indexed elements
n = int(input("Enter number of elements in the list: "))
lst = []
for i in range(n):
    num = int(input("Enter element {}: ".format(i+1)))
    lst.append(num)
sum_even_indexed = 0
for i in range(0, n, 2):
    sum_even_indexed += lst[i]
print("Sum of even-indexed elements in the list:", sum_even_indexed)