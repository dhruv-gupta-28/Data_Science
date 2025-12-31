# 1. Reverse a number
# Input: 1234 → Output: 4321

num = int(input("Enter a number: "))
original = num
reverse = 0

while num > 0:
    remainder = num % 10
    reverse = reverse * 10 + remainder
    num = num // 10

print(f"Original number: {original}")
print(f"Reversed number: {reverse}")

