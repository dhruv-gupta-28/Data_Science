"""
Python Fundamentals: Control Flow - If/Else Statements
======================================================

Topics Covered:
- if statement
- if-else statement
- if-elif-else statement
- Nested if statements
- Ternary operator
"""

# ============================================================================
# 1. SIMPLE IF STATEMENT
# ============================================================================

age = 20

print("--- Simple If Statement ---")
if age >= 18:
    print(f"You are {age} years old - an adult")
if age < 18:
    print(f"You are {age} years old - a minor")

# ============================================================================
# 2. IF-ELSE STATEMENT
# ============================================================================

score = 45

print(f"\n--- If-Else Statement ---")
if score >= 50:
    print(f"Score: {score} - PASSED")
else:
    print(f"Score: {score} - FAILED")

# ============================================================================
# 3. IF-ELIF-ELSE STATEMENT
# ============================================================================

grade_points = 85

print(f"\n--- If-Elif-Else Statement ---")
if grade_points >= 90:
    grade = 'A'
elif grade_points >= 80:
    grade = 'B'
elif grade_points >= 70:
    grade = 'C'
elif grade_points >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"Points: {grade_points} - Grade: {grade}")

# ============================================================================
# 4. NESTED IF STATEMENTS
# ============================================================================

temperature = 35
is_humid = True

print(f"\n--- Nested If Statements ---")
if temperature > 30:
    print("It's hot outside")
    if is_humid:
        print("And it's humid - very uncomfortable!")
    else:
        print("But it's dry - bearable")
else:
    print("It's cool/cold outside")

# ============================================================================
# 5. TERNARY OPERATOR (CONDITIONAL EXPRESSION)
# ============================================================================

num = 15

print(f"\n--- Ternary Operator ---")
result = "Even" if num % 2 == 0 else "Odd"
print(f"{num} is {result}")

status = "Pass" if score >= 50 else "Fail"
print(f"Score {score}: {status}")

# ============================================================================
# 6. PRACTICAL EXAMPLES
# ============================================================================

print(f"\n--- Practical Examples ---")

# Example 1: Age category
print("\nExample 1: Age Category")
user_age = 25
if user_age < 13:
    category = "Child"
elif user_age < 18:
    category = "Teenager"
elif user_age < 60:
    category = "Adult"
else:
    category = "Senior"
print(f"Age {user_age} is {category}")

# Example 2: Login validation
print("\nExample 2: Login Validation")
username = "admin"
password = "password123"
input_user = "admin"
input_pass = "password123"

if input_user == username and input_pass == password:
    print("Login successful!")
else:
    print("Invalid credentials!")

# Example 3: Number range check
print("\nExample 3: Number Range Check")
number = 50
if 0 <= number <= 100:
    print(f"{number} is between 0 and 100")
else:
    print(f"{number} is outside the range")

# ============================================================================
# 7. PRACTICE PROBLEMS
# ============================================================================

print(f"\n--- Practice Problems ---")

# Problem 1: Determine eligibility for voting
print("\nProblem 1: Voting Eligibility")
voter_age = 22
if voter_age >= 18:
    print(f"Age {voter_age}: Eligible to vote")
else:
    print(f"Age {voter_age}: Not eligible to vote")

# Problem 2: Classify triangle by sides
print("\nProblem 2: Triangle Classification")
side1, side2, side3 = 5, 5, 8
if side1 == side2 == side3:
    triangle = "Equilateral"
elif side1 == side2 or side2 == side3 or side1 == side3:
    triangle = "Isosceles"
else:
    triangle = "Scalene"
print(f"Sides {side1}, {side2}, {side3}: {triangle} triangle")

# Problem 3: Determine if number is positive, negative, or zero
print("\nProblem 3: Number Sign")
test_num = -15
if test_num > 0:
    sign = "Positive"
elif test_num < 0:
    sign = "Negative"
else:
    sign = "Zero"
print(f"Number {test_num} is {sign}")

# ============================================================================
# 8. CHALLENGES
# ============================================================================

print(f"\n--- Challenges ---")

# Challenge 1: Leap year checker
print("\nChallenge 1: Leap Year Checker")
# TODO: Check if a year is a leap year
# A year is a leap year if:
# - It's divisible by 4 AND not divisible by 100
# - OR it's divisible by 400

# Challenge 2: Find maximum of three numbers
print("\nChallenge 2: Maximum of Three Numbers")
# TODO: Find and print the maximum of three numbers

# Challenge 3: Traffic light simulator
print("\nChallenge 3: Traffic Light")
# TODO: Given a color (red/yellow/green), print corresponding action
