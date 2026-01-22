# 69. Dictionary of Primes
# Input: Numbers 1–10
# Output: {1:False, 2:True, 3:True, 4:False, ..., 10:False}

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

d = {}
for i in range(1, 11):
    d[i] = is_prime(i)
print(d)

