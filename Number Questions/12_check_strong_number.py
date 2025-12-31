# 12. Check if a number is strong or not
# Example: 145 → 1! + 4! + 5! = 145 ✅

def factorial(n):
    """Calculate factorial of a number"""
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

num = int(input("Enter a number: "))
original = num
sum_factorials = 0

while num > 0:
    digit = num % 10
    sum_factorials += factorial(digit)
    num = num // 10

if original == sum_factorials:
    print(f"{original} is a strong number.")
else:
    print(f"{original} is not a strong number.")

