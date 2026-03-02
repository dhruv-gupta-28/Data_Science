"""
Python Fundamentals: Loops - For and While
===========================================

Topics Covered:
- for loop basics
- while loop
- break and continue statements  
- Loop control
- Nested loops
"""

# ============================================================================
# 1. FOR LOOP - RANGE
# ============================================================================

print("--- For Loop with range ---")

# Basic for loop
for i in range(5):
    print(f"Iteration {i}")

# With start and end
print("\nFor loop 2-5:")
for i in range(2, 6):
    print(i, end=" ")
print()

# With step
print("\nFor loop 0-10 step 2:")
for i in range(0, 11, 2):
    print(i, end=" ")
print()

# ============================================================================
# 2. FOR LOOP - ITERATING OVER SEQUENCES
# ============================================================================

print("\n--- Iterating Over Sequences ---")

# Over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

# Over a string
word = "Python"
print(f"\nLetters in '{word}':")
for letter in word:
    print(letter, end=" ")
print()

# Using enumerate
print("\n\nWith enumerate:")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# ============================================================================
# 3. WHILE LOOP
# ============================================================================

print(f"\n--- While Loop ---")

count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# While with string input simulation
print("\nPassword attempt simulation:")
attempts = 0
while attempts < 3:
    print(f"Attempt {attempts + 1}:")
    attempts += 1

# ============================================================================
# 4. BREAK STATEMENT
# ============================================================================

print(f"\n--- Break Statement ---")

print("Search for number 5:")
for num in range(1, 10):
    if num == 5:
        print(f"Found {num}!")
        break
    print(num, end=" ")

# ============================================================================
# 5. CONTINUE STATEMENT
# ============================================================================

print(f"\n--- Continue Statement ---")

print("Print even numbers 1-10:")
for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i, end=" ")
print()

# ============================================================================
# 6. NESTED LOOPS
# ============================================================================

print(f"\n--- Nested Loops ---")

print("Multiplication table (2x3):")
for i in range(1, 3):
    for j in range(1, 4):
        print(f"{i}x{j}={i*j}", end="  ")
    print()

# Pattern printing
print("\nTriangle pattern:")
for i in range(1, 4):
    for j in range(i):
        print("*", end="")
    print()

# ============================================================================
# 7. ELSE WITH LOOPS
# ============================================================================

print(f"\n--- Else with Loops ---")

# Else executes when loop completes normally
print("For loop with else:")
for i in range(3):
    print(i)
else:
    print("Loop completed!")

# Else doesn't execute if loop breaks
print("\nFor loop with break (no else):")
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("This won't print")

# ============================================================================
# 8. PRACTICE PROBLEMS
# ============================================================================

print(f"\n--- Practice Problems ---")

# Problem 1: Sum of numbers
print("\nProblem 1: Sum of numbers 1-10")
total = 0
for num in range(1, 11):
    total += num
print(f"Sum: {total}")

# Problem 2: Print squares
print("\nProblem 2: Print squares 1-5")
for num in range(1, 6):
    print(f"{num}^2 = {num**2}")

# Problem 3: Countdown
print("\nProblem 3: Countdown from 5")
for i in range(5, -1, -1):
    print(i, end=" ")
print("\nBlastoff!")

# Problem 4: Star pattern
print("\nProblem 4: Square pattern (3x3):")
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()

# ============================================================================
# 9. CHALLENGES
# ============================================================================

print(f"\n--- Challenges ---")

# Challenge 1: Factorial calculation
print("\nChallenge 1: Calculate factorial")
# TODO: Calculate factorial of 5 (5! = 5*4*3*2*1)

# Challenge 2: Find prime numbers
print("\nChallenge 2: Find prime numbers 1-20")
# TODO: Find and print all prime numbers between 1 and 20

# Challenge 3: FizzBuzz
print("\nChallenge 3: FizzBuzz (1-15)")
# TODO: Print numbers, but print "Fizz" for multiples of 3,
#       "Buzz" for multiples of 5, "FizzBuzz" for both
