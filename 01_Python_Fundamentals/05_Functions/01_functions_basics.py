"""
Python Fundamentals: Functions
=============================

Topics Covered:
- Function definition
- Parameters and arguments
- Return values
- Default parameters
- *args and **kwargs
- Variable scope
- Lambda functions
"""

# ============================================================================
# 1. BASIC FUNCTION
# ============================================================================

def greet():
    """Simple function that prints a greeting"""
    print("Hello, World!")

print("--- Basic Function ---")
greet()

# ============================================================================
# 2. FUNCTION WITH PARAMETERS
# ============================================================================

def greet_person(name):
    """Function with one parameter"""
    print(f"Hello, {name}!")

print("\n--- Function with Parameters ---")
greet_person("Alice")
greet_person("Bob")

# Multiple parameters
def add(a, b):
    """Add two numbers"""
    print(f"{a} + {b} = {a + b}")

add(5, 3)

# ============================================================================
# 3. RETURN VALUES
# ============================================================================

def multiply(x, y):
    """Return the product of two numbers"""
    return x * y

print(f"\n--- Return Values ---")
result = multiply(4, 5)
print(f"Result: {result}")

# Function returning multiple values
def divide_with_remainder(a, b):
    """Return quotient and remainder"""
    return a // b, a % b

quotient, remainder = divide_with_remainder(10, 3)
print(f"10 ÷ 3 = {quotient} remainder {remainder}")

# ============================================================================
# 4. DEFAULT PARAMETERS
# ============================================================================

def power(base, exponent=2):
    """Raise base to power (default is 2)"""
    return base ** exponent

print(f"\n--- Default Parameters ---")
print(f"5^2 = {power(5)}")
print(f"5^3 = {power(5, 3)}")

# ============================================================================
# 5. KEYWORD ARGUMENTS
# ============================================================================

def introduce(first_name, last_name, age, city="Unknown"):
    """Introduce a person"""
    print(f"{first_name} {last_name}, {age} years old from {city}")

print(f"\n--- Keyword Arguments ---")
introduce("John", "Doe", 30, "New York")
introduce(first_name="Jane", last_name="Smith", age=28, city="Boston")
introduce("Bob", "Johnson", 25)

# ============================================================================
# 6. *args (VARIABLE POSITIONAL ARGUMENTS)
# ============================================================================

def sum_all(*numbers):
    """Sum any number of arguments"""
    total = sum(numbers)
    return total

print(f"\n--- *args ---")
print(f"sum_all(1, 2, 3) = {sum_all(1, 2, 3)}")
print(f"sum_all(1, 2, 3, 4, 5) = {sum_all(1, 2, 3, 4, 5)}")

# ============================================================================
# 7. **kwargs (KEYWORD ARGUMENTS)
# ============================================================================

def print_info(**info):
    """Print key-value pairs"""
    for key, value in info.items():
        print(f"{key}: {value}")

print(f"\n--- **kwargs ---")
print_info(name="Alice", age=25, city="NYC")
print_info(product="Laptop", price=1000, brand="Dell")

# ============================================================================
# 8. DOCSTRINGS AND TYPE HINTS
# ============================================================================

def calculate_area(length: float, width: float) -> float:
    """
    Calculate rectangle area.
    
    Args:
        length: The length of the rectangle
        width: The width of the rectangle
    
    Returns:
        float: The area of the rectangle
    """
    return length * width

print(f"\n--- Docstrings ---")
print(f"Area of 5x4 rectangle: {calculate_area(5, 4)}")
print(f"Help: {calculate_area.__doc__}")

# ============================================================================
# 9. LAMBDA FUNCTIONS
# ============================================================================

print(f"\n--- Lambda Functions ---")

# Simple lambda
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

# Lambda in map
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(f"Squares: {squared}")

# Lambda in sorted
students = [("Alice", 85), ("Bob", 90), ("Charlie", 78)]
sorted_by_score = sorted(students, key=lambda x: x[1], reverse=True)
print(f"Students by score: {sorted_by_score}")

# ============================================================================
# 10. VARIABLE SCOPE
# ============================================================================

print(f"\n--- Variable Scope ---")

global_var = "I'm global"

def scope_example():
    local_var = "I'm local"
    print(f"Inside function: {global_var}, {local_var}")

scope_example()
print(f"Outside function: {global_var}")
# print(local_var)  # This would error - local_var not defined outside function

# ============================================================================
# 11. PRACTICE PROBLEMS
# ============================================================================

print(f"\n--- Practice Problems ---")

# Problem 1: Palindrome checker
print("\nProblem 1: Palindrome Checker")
def is_palindrome(text):
    """Check if text is a palindrome"""
    text = text.lower().replace(" ", "")
    return text == text[::-1]

print(f"'racecar' is palindrome: {is_palindrome('racecar')}")
print(f"'hello' is palindrome: {is_palindrome('hello')}")

# Problem 2: Temperature converter
print("\nProblem 2: Temperature Converter")
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

print(f"0°C = {celsius_to_fahrenheit(0)}°F")
print(f"25°C = {celsius_to_fahrenheit(25)}°F")

# Problem 3: List operations
print("\nProblem 3: List Operations")
def list_stats(numbers):
    """Return min, max, and average"""
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

data = [1, 5, 3, 9, 2]
min_val, max_val, avg = list_stats(data)
print(f"Min: {min_val}, Max: {max_val}, Avg: {avg:.2f}")

# ============================================================================
# 12. CHALLENGES
# ============================================================================

print(f"\n--- Challenges ---")

# Challenge 1: Fibonacci generator
print("\nChallenge 1: Fibonacci")
# TODO: Create function to return the nth Fibonacci number

# Challenge 2: Prime checker
print("\nChallenge 2: Prime Checker")
# TODO: Check if number is prime

# Challenge 3: Password validator
print("\nChallenge 3: Password Validator")
# TODO: Validate password (min 8 chars, at least one uppercase, one digit)
