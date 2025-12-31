# 13. Find the sum of first N natural numbers.

n = int(input("Enter a number N: "))
sum_n = 0

for i in range(1, n + 1):
    sum_n += i

print(f"Sum of first {n} natural numbers is: {sum_n}")

