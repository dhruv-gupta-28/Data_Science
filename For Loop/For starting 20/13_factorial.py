# 13. Find the factorial of a number n.

n = int(input("Enter a number to find its factorial: "))
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"The factorial of {n} is {factorial}")
