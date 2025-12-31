# 14. Find the sum of even and odd numbers separately up to N.

n = int(input("Enter a number N: "))
sum_even = 0
sum_odd = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i

print(f"Sum of even numbers up to {n}: {sum_even}")
print(f"Sum of odd numbers up to {n}: {sum_odd}")

