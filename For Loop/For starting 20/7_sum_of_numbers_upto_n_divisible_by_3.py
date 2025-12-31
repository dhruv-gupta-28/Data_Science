# 7. Find the sum of all numbers from 1 to n that are divisible by 3.

n = int(input("Enter a number: "))
sum_divisible_by_3 = 0

for i in range(1, n + 1):
    if i % 3 == 0:
        sum_divisible_by_3 += i

print(f"The sum of all numbers from 1 to {n} that are divisible by 3 is: {sum_divisible_by_3}")
