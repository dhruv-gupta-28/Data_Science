# 10. Check if a number is perfect or not
# Example: 6 → 1 + 2 + 3 = 6 ✅

num = int(input("Enter a number: "))
sum_of_factors = 0

for i in range(1, num):
    if num % i == 0:
        sum_of_factors += i

if sum_of_factors == num:
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")

