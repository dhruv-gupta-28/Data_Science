"""
Python Fundamentals: Input and Output
=====================================

Topics Covered:
- input() function
- print() function and formatting
- String formatting (f-strings, format(), %)
- File output basics
- User interaction patterns
"""

# ============================================================================
# 1. INPUT FUNCTION
# ============================================================================

print("--- Basic Input ---")

# Simple input
# name = input("What is your name? ")
# print(f"Hello, {name}!")

# Input with type conversion
# age_str = input("Enter your age: ")
# age = int(age_str)
# print(f"You are {age} years old")

# ============================================================================
# 2. PRINT FUNCTION BASICS
# ============================================================================

print("\n--- Print Function ---")

# Basic print
print("Hello, World!")

# Multiple arguments
print("Name:", "Alice", "Age:", 25)

# With sep parameter (separator)
print("A", "B", "C", sep="-")
print(1, 2, 3, sep=" | ")

# With end parameter
print("Loading", end="")
print(".", end="")
print(".", end="")
print("Done!")

# ============================================================================
# 3. F-STRING FORMATTING (MODERN)
# ============================================================================

print("\n--- F-String Formatting ---")

name = "Bob"
age = 30
height = 5.9

# Basic f-string
print(f"Name: {name}, Age: {age}, Height: {height}")

# With expressions
print(f"Next year: {age + 1}")
print(f"Height in cm: {height * 30.48:.1f}")

# Alignment
print(f"{'Left':<10} {'Center':^10} {'Right':>10}")

# ============================================================================
# 4. .FORMAT() METHOD
# ============================================================================

print("\n--- Format Method ---")

# Positional arguments
print("Hello {} {}".format("John", "Doe"))

# With indices
print("{1} {0}".format("Smith", "Jane"))

# Named arguments
print("{name} is {age} years old".format(name="Charlie", age=35))

# ============================================================================
# 5. % FORMATTING (OLD STYLE)
# ============================================================================

print("\n--- % Formatting ---")

name = "Diana"
score = 95.5

print("Name: %s, Score: %d" % (name, int(score)))
print("Score: %.1f%%" % score)

# ============================================================================
# 6. INPUT VALIDATION
# ============================================================================

print("\n--- Input Validation Example ---")

def get_positive_integer():
    """Get positive integer from user"""
    while True:
        try:
            num = int(input("Enter a positive integer: "))
            if num > 0:
                return num
            else:
                print("Please enter a positive number")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Uncomment to test:
# positive_num = get_positive_integer()
# print(f"You entered: {positive_num}")

# ============================================================================
# 7. MULTIPLE INPUTS
# ============================================================================

print("\n--- Multiple Inputs Example ---")

# Simulated input for demonstration
inputs = ["25", "John", "Engineer"]
input_iter = iter(inputs)

def simulated_input(prompt):
    """Simulate input for testing"""
    print(prompt, end="")
    return next(input_iter)

# Example usage pattern:
# age = int(simulated_input("Age: "))
# name = simulated_input("Name: ")
# job = simulated_input("Job: ")

# ============================================================================
# 8. FORMATTED OUTPUT
# ============================================================================

print("\n--- Formatted Output Examples ---")

# Table formatting
print("\nStudent Grades Table:")
print(f"{'Name':<15} {'Math':<10} {'English':<10} {'Science':<10}")
print("-" * 45)
print(f"{'Alice':<15} {'95':<10} {'88':<10} {'92':<10}")
print(f"{'Bob':<15} {'87':<10} {'91':<10} {'85':<10}")
print(f"{'Charlie':<15} {'92':<10} {'89':<10} {'94':<10}")

# Currency formatting
amount = 1234.5678
print(f"\nAmount: ${amount:,.2f}")

# Percentage formatting
percentage = 0.857
print(f"Percentage: {percentage:.1%}")

# ============================================================================
# 9. PRACTICE PROBLEMS
# ============================================================================

print("\n--- Practice Problems ---")

# Problem 1: Personal information input
print("\nProblem 1: Create a profile")
# TODO: Ask for name, age, email and display formatted

# Problem 2: Simple calculator
print("\nProblem 2: Simple Calculator")
# TODO: Ask for two numbers and operation, then calculate

# Problem 3: Grade calculator
print("\nProblem 3: Grade Calculator")
# TODO: Ask for marks in 5 subjects, calculate average and grade

# ============================================================================
# 10. CHALLENGES
# ============================================================================

print("\n--- Challenges ---")

# Challenge 1: Rectangle dimensions
print("\nChallenge 1: Rectangle Calculator")
# TODO: Ask for length and width, calculate and display area and perimeter

# Challenge 2: Temperature converter GUI simulation
print("\nChallenge 2: Temperature Converter")
# TODO: Ask for temp in C, convert to F, display nicely formatted

# Challenge 3: Budget tracker
print("\nChallenge 3: Budget Tracker")
# TODO: Ask for income and expenses, show remaining budget formatted
