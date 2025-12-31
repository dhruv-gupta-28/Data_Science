# 14. Print all numbers between 1 and n that are divisible by both 3 and 5.

n = int(input("Enter a number: "))

print(f"Numbers between 1 and {n} that are divisible by both 3 and 5:")
for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
