# 8. Find the sum of all numbers from 1 to n that are divisible by 5.

n = int(input("Enter a number: "))
sum_divisible_by_5 = 0

for i in range(1, n + 1):
    if i % 5 == 0:
        sum_divisible_by_5 += i

print(f"The sum of all numbers from 1 to {n} that are divisible by 5 is: {sum_divisible_by_5}")
