# 19. Find the sum of all prime numbers between 1 and n.

n = int(input("Enter a number: "))
sum_primes = 0

for i in range(2, n + 1):
    is_prime = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        sum_primes += i

print(f"The sum of all prime numbers between 1 and {n} is: {sum_primes}")
