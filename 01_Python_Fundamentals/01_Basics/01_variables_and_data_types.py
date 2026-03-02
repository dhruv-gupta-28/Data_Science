"""
Python Fundamentals: Variables and Data Types
==============================================

Topics Covered:
- Variable declaration and assignment
- Data types: int, float, str, bool
- Type checking with type()
- Type conversion
- Constants and naming conventions
"""

# ============================================================================
# 1. VARIABLES AND ASSIGNMENT
# ============================================================================

# Variables store data values
name = "Alice"
age = 25
height = 5.9
is_student = True

print(f"Name: {name}, Age: {age}, Height: {height}, Student: {is_student}")

# ============================================================================
# 2. DATA TYPES
# ============================================================================

# Integer - whole numbers
count = 100
negative = -50
zero = 0

# Float - decimal numbers
pi = 3.14159
temperature = -40.5

# String - text (sequence of characters)
greeting = "Hello, World!"
multi_line = """This is a
multi-line
string"""

# Boolean - True or False
is_valid = True
is_empty = False

# ============================================================================
# 3. TYPE CHECKING
# ============================================================================

print("\n--- Type Checking ---")
print(f"type(count) = {type(count)}")           # <class 'int'>
print(f"type(pi) = {type(pi)}")                 # <class 'float'>
print(f"type(greeting) = {type(greeting)}")     # <class 'str'>
print(f"type(is_valid) = {type(is_valid)}")     # <class 'bool'>

# ============================================================================
# 4. TYPE CONVERSION (CASTING)
# ============================================================================

# Convert string to integer
num_string = "42"
num_int = int(num_string)
print(f"\nString '{num_string}' converted to int: {num_int}")

# Convert to string
age_str = str(age)
print(f"Age as string: {age_str}, type: {type(age_str)}")

# Convert to float
height_float = float("5.9")
print(f"Height as float: {height_float}")

# Convert to boolean
print(f"bool(0) = {bool(0)}")      # False
print(f"bool(1) = {bool(1)}")      # True
print(f"bool('') = {bool('')}")    # False
print(f"bool('hello') = {bool('hello')}")  # True

# ============================================================================
# 5. NAMING CONVENTIONS
# ============================================================================

# Valid variable names
valid_name = "Valid"
_private_var = "Private"
thisIsAVariable = "Camel case"
THIS_IS_CONSTANT = 3.14159  # Convention: ALL_CAPS for constants

# ============================================================================
# 6. MULTIPLE ASSIGNMENT
# ============================================================================

x, y, z = 1, 2, 3
print(f"\nMultiple assignment: x={x}, y={y}, z={z}")

# Swapping values
a, b = 10, 20
a, b = b, a  # Swap
print(f"After swap: a={a}, b={b}")

# ============================================================================
# 7. PRACTICE PROBLEMS
# ============================================================================

print("\n--- Practice Problems ---")

# Problem 1: Create variables and print their types
favorite_food = "Pizza"
servings = 2
price = 12.99
is_delivery = True

print(f"\nProblem 1:")
print(f"Food: {favorite_food} ({type(favorite_food).__name__})")
print(f"Servings: {servings} ({type(servings).__name__})")
print(f"Price: ${price} ({type(price).__name__})")
print(f"Delivery: {is_delivery} ({type(is_delivery).__name__})")

# Problem 2: Type conversion practice
age_input = "30"
birth_year_input = "1994"
age_conversion = int(age_input)
birth_year_conversion = int(birth_year_input)
print(f"\nProblem 2:")
print(f"Age: {age_conversion}, Birth Year: {birth_year_conversion}")

# Problem 3: Calculate BMI
weight_kg = 70
height_m = 1.75
bmi = weight_kg / (height_m ** 2)
print(f"\nProblem 3:")
print(f"Weight: {weight_kg}kg, Height: {height_m}m, BMI: {bmi:.2f}")

# ============================================================================
# 8. CHALLENGES
# ============================================================================

print("\n--- Challenges ---")

# Challenge 1: Create variables for personal information and display
print("\nChallenge 1: Personal Information")
# TODO: Create variables for name, email, phone, city, country
# Try to print them in a formatted way

# Challenge 2: Convert and calculate
print("\nChallenge 2: Temperature Conversion")
# TODO: Take a temperature in Celsius, convert to Fahrenheit
# Formula: F = (C × 9/5) + 32

# Challenge 3: String to number conversion with validation
print("\nChallenge 3: Validate Input")
# TODO: Take string input, convert to int, handle potential errors
