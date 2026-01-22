#Count primes in a list
n = int(input("Enter number of elements in the list: "))
lst = []
for i in range(n):
    num = int(input("Enter element {}: ".format(i+1)))
    lst.append(num)
prime_count = 0
for num in lst:
    if num > 1:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_count += 1
print("Number of prime numbers in the list:", prime_count)