# 31. Count primes in a list
# Input: [2, 3, 4, 5, 6, 7, 9]
# Output: 4

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))
    lst.append(ele)

prime_count = 0
for num in lst:
    if is_prime(num):
        prime_count += 1

print(f"Count of prime numbers: {prime_count}")

