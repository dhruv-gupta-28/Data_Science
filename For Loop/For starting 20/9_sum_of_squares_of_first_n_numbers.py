# 9. Find the sum of squares of the first n natural numbers.

n = int(input("Enter a number: "))
sum_squares = 0

for i in range(1, n + 1):
    sum_squares += i ** 2

print(f"The sum of squares of the first {n} natural numbers is: {sum_squares}")
