# 18. Find the product of all even numbers from 1 to n.

n = int(input("Enter a number: "))
product = 1

for i in range(2, n + 1, 2):
    product *= i

print(f"The product of all even numbers from 1 to {n} is: {product}")
