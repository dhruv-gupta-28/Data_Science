# 3. Check if a number is Armstrong
# 153 → 1³ + 5³ + 3³ = 153 ✅

num = int(input("Enter a number: "))
original = num
sum_of_cubes = 0
num_digits = len(str(num))

while num > 0:
    digit = num % 10
    sum_of_cubes += digit ** num_digits
    num = num // 10

if original == sum_of_cubes:
    print(f"{original} is an Armstrong number.")
else:
    print(f"{original} is not an Armstrong number.")

