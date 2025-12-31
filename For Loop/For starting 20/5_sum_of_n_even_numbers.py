# 5. Find the sum of the first n even numbers.

n = int(input("Enter a number: "))
sum_even = 0

for i in range(2, 2 * n + 1, 2):
    sum_even += i

print(f"The sum of the first {n} even numbers is: {sum_even}")
