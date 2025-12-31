# 15. Print all numbers between 1 and n that are not divisible by 2.

n = int(input("Enter a number: "))

print(f"Numbers between 1 and {n} that are not divisible by 2:")
for i in range(1, n + 1):
    if i % 2 != 0:
        print(i)
