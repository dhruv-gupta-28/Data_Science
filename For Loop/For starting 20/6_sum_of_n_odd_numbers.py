# 6. Find the sum of the first n odd numbers.

n = int(input("Enter a number: "))
sum_odd = 0

for i in range(1, 2 * n, 2):
    sum_odd += i

print(f"The sum of the first {n} odd numbers is: {sum_odd}")
