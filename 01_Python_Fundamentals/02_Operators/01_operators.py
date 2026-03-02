"""
Python Fundamentals: Operators
==============================

Topics Covered:
- Arithmetic operators (+, -, *, /, //, %, **)
- Comparison operators (==, !=, <, >, <=, >=)
- Logical operators (and, or, not)
- Assignment operators (=, +=, -=, *=, /=)
- Operator precedence
"""

# ============================================================================
# 1. ARITHMETIC OPERATORS
# ============================================================================

a = 10
b = 3

print("--- Arithmetic Operators ---")
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Exponentiation: {a} ** {b} = {a ** b}")

# ============================================================================
# 2. COMPARISON OPERATORS
# ============================================================================

x = 5
y = 8

print(f"\n--- Comparison Operators ---")
print(f"{x} == {y}: {x == y}")      # Equal to
print(f"{x} != {y}: {x != y}")      # Not equal
print(f"{x} < {y}: {x < y}")        # Less than
print(f"{x} > {y}: {x > y}")        # Greater than
print(f"{x} <= {y}: {x <= y}")      # Less than or equal
print(f"{x} >= {y}: {x >= y}")      # Greater than or equal

# ============================================================================
# 3. LOGICAL OPERATORS
# ============================================================================

p = True
q = False

print(f"\n--- Logical Operators ---")
print(f"True and False: {p and q}")
print(f"True or False: {p or q}")
print(f"not True: {not p}")
print(f"not False: {not q}")

# More complex logic
age = 25
has_license = True
can_drive = (age >= 18) and has_license
print(f"\nAge: {age}, Has License: {has_license}")
print(f"Can Drive: {can_drive}")

# ============================================================================
# 4. ASSIGNMENT OPERATORS
# ============================================================================

num = 10
print(f"\n--- Assignment Operators ---")
print(f"Initial: num = {num}")

num += 5
print(f"After += 5: num = {num}")

num -= 3
print(f"After -= 3: num = {num}")

num *= 2
print(f"After *= 2: num = {num}")

num //= 4
print(f"After //= 4: num = {num}")

# ============================================================================
# 5. OPERATOR PRECEDENCE
# ============================================================================

print(f"\n--- Operator Precedence ---")
# PEMDAS: Parentheses, Exponents, Multiplication/Division, Addition/Subtraction

result1 = 2 + 3 * 4
result2 = (2 + 3) * 4

print(f"2 + 3 * 4 = {result1}")      # 14 (multiplication first)
print(f"(2 + 3) * 4 = {result2}")    # 20 (parentheses first)

result3 = 10 - 2 ** 2
result4 = (10 - 2) ** 2

print(f"10 - 2 ** 2 = {result3}")    # 6 (exponent first)
print(f"(10 - 2) ** 2 = {result4}")  # 64 (parentheses first)

# ============================================================================
# 6. PRACTICE PROBLEMS
# ============================================================================

print(f"\n--- Practice Problems ---")

# Problem 1: Calculate basic arithmetic
print("\nProblem 1: Basic Arithmetic")
num1, num2 = 15, 4
print(f"Numbers: {num1}, {num2}")
print(f"Sum: {num1 + num2}")
print(f"Product: {num1 * num2}")
print(f"Division: {num1 / num2}")
print(f"Remainder: {num1 % num2}")

# Problem 2: Compare two numbers
print("\nProblem 2: Number Comparison")
num1, num2 = 20, 30
print(f"{num1} < {num2}: {num1 < num2}")
print(f"{num1} == {num2}: {num1 == num2}")
print(f"{num1} > {num2}: {num1 > num2}")

# Problem 3: Check conditions
print("\nProblem 3: Conditional Logic")
score = 75
passed = score >= 50
excellent = score >= 90
print(f"Score: {score}")
print(f"Passed (>=50): {passed}")
print(f"Excellent (>=90): {excellent}")

# Problem 4: Complex expression
print("\nProblem 4: Complex Expression")
a, b, c = 10, 20, 30
result = a + b * c - a / b
print(f"a={a}, b={b}, c={c}")
print(f"a + b * c - a / b = {result}")

# ============================================================================
# 7. CHALLENGES
# ============================================================================

print("\n--- Challenges ---")

# Challenge 1: BMI calculation
print("\nChallenge 1: BMI Category")
# TODO: Calculate BMI and determine category (underweight, normal, overweight, obese)

# Challenge 2: Grade evaluation
print("\nChallenge 2: Grade Evaluation")
# TODO: Given marks out of 100, determine if passed and print grade

# Challenge 3: Eligible for discount
print("\nChallenge 3: Discount Eligibility")
# TODO: Check if customer qualifies for discount (age > 60 OR purchase > 1000)
