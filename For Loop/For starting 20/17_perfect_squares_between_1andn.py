# 17. Count how many numbers between 1 and n are perfect squares.

n = int(input("Enter a number: "))
count = 0

for i in range(1, n + 1):
    # Check if i is a perfect square
    root = int(i ** 0.5)
    if root * root == i:
        count += 1

print(f"The number of perfect squares between 1 and {n} is: {count}")
