# 16. Print the Fibonacci series up to n terms.

n = int(input("Enter the number of terms: "))

if n <= 0:
    print("Please enter a positive integer")
elif n == 1:
    print("Fibonacci sequence up to 1 term:")
    print(0)
else:
    print("Fibonacci sequence:")
    a, b = 0, 1
    for i in range(n):
        print(a)
        a, b = b, a + b
