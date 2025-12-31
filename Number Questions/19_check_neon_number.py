# 19. Check if a number is Neon number
# Square of number's digits sum equals number
# Example: 9² = 81 → 8 + 1 = 9 ✅

num = int(input("Enter a number: "))
square = num ** 2
sum_digits = 0

while square > 0:
    digit = square % 10
    sum_digits += digit
    square = square // 10

if num == sum_digits:
    print(f"{num} is a Neon number.")
else:
    print(f"{num} is not a Neon number.")

