# 10. Find the sum of cubes of the first n natural numbers.

n = int(input("Enter a number: "))
sum_cubes = 0

for i in range(1, n + 1):
    sum_cubes += i ** 3

print(f"The sum of cubes of the first {n} natural numbers is: {sum_cubes}")
