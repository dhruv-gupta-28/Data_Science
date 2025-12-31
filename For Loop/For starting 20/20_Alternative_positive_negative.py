# 20. Print all numbers between 1 and n in this pattern: positive and negative alternate (e.g., 1 -2 3 -4 5 -6 ...)

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    if i % 2 == 0:
        print(-i, end=' ')
    else:
        print(i, end=' ')

print()  # New line at the end
