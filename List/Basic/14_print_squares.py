# 14. Print squares
# Input: [1, 2, 3, 4]
# Output: [1, 4, 9, 16]

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))
    lst.append(ele)

squares = []
for num in lst:
    squares.append(num ** 2)

print(f"Squares: {squares}")

