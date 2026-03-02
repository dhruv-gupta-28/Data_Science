"""
Python Fundamentals: Data Structures - Tuples
==============================================

Topics Covered:
- Creating tuples
- Accessing tuple elements
- Tuple operations
- Tuple methods
- Tuples vs Lists (immutability)
- Tuple unpacking
"""

# ============================================================================
# 1. CREATING TUPLES
# ============================================================================

print("--- Creating Tuples ---")

# Empty tuple
empty_tuple = ()

# Single element tuple (note the comma!)
single = (1,)
single_no_paren = 1,  # Same as above

# Multiple elements
coordinates = (10, 20)
rgb_color = (255, 128, 0)
mixed = (1, "hello", 3.14, True)

# Without parentheses (implicit tuple)
point = 5, 10, 15

print(f"Empty: {empty_tuple}")
print(f"Single: {single}")
print(f"Coordinates: {coordinates}")
print(f"Mixed: {mixed}")

# ============================================================================
# 2. ACCESSING TUPLE ELEMENTS
# ============================================================================

print(f"\n--- Accessing Elements ---")

colors = ("red", "green", "blue", "yellow")

print(f"First color: {colors[0]}")
print(f"Last color: {colors[-1]}")
print(f"Second color: {colors[1]}")

# ============================================================================
# 3. TUPLE SLICING
# ============================================================================

print(f"\n--- Tuple Slicing ---")

numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

print(f"First 5: {numbers[:5]}")
print(f"From index 3 to 7: {numbers[3:7]}")
print(f"Every 2nd number: {numbers[::2]}")
print(f"Reversed: {numbers[::-1]}")

# ============================================================================
# 4. TUPLE OPERATIONS
# ============================================================================

print(f"\n--- Tuple Operations ---")

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenation
combined = tuple1 + tuple2
print(f"Concatenation: {combined}")

# Repetition
repeated = tuple1 * 3
print(f"Repetition: {repeated}")

# Length
print(f"Length: {len(tuple1)}")

# Membership
print(f"2 in tuple1: {2 in tuple1}")
print(f"10 in tuple1: {10 in tuple1}")

# ============================================================================
# 5. TUPLE METHODS
# ============================================================================

print(f"\n--- Tuple Methods ---")

numbers = (1, 2, 3, 2, 4, 2, 5)

# Count
count_2 = numbers.count(2)
print(f"Count of 2: {count_2}")

# Index
index_3 = numbers.index(3)
print(f"Index of 3: {index_3}")

# ============================================================================
# 6. TUPLE UNPACKING
# ============================================================================

print(f"\n--- Tuple Unpacking ---")

# Basic unpacking
coordinates = (10, 20, 30)
x, y, z = coordinates
print(f"x={x}, y={y}, z={z}")

# Extended unpacking
data = (1, 2, 3, 4, 5)
first, *middle, last = data
print(f"First: {first}, Middle: {middle}, Last: {last}")

# Swapping values
a, b = 5, 10
a, b = b, a
print(f"After swap: a={a}, b={b}")

# ============================================================================
# 7. TUPLES VS LISTS
# ============================================================================

print(f"\n--- Tuples vs Lists ---")

# Lists are mutable
list_data = [1, 2, 3]
list_data[0] = 100
print(f"Modified list: {list_data}")

# Tuples are immutable
tuple_data = (1, 2, 3)
try:
    tuple_data[0] = 100
except TypeError as e:
    print(f"Cannot modify tuple: {e}")

# ============================================================================
# 8. RETURNING MULTIPLE VALUES
# ============================================================================

print(f"\n--- Returning Multiple Values ---")

def get_coordinates():
    """Return multiple values as tuple"""
    return 10, 20, 30

x, y, z = get_coordinates()
print(f"Coordinates: x={x}, y={y}, z={z}")

def min_max(numbers):
    """Return minimum and maximum"""
    return min(numbers), max(numbers)

data = [5, 2, 9, 1, 7]
minimum, maximum = min_max(data)
print(f"Min: {minimum}, Max: {maximum}")

# ============================================================================
# 9. NESTED TUPLES
# ============================================================================

print(f"\n--- Nested Tuples ---")

matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

print("Matrix:")
for row in matrix:
    print(row)

print(f"Element [1][2]: {matrix[1][2]}")

# ============================================================================
# 10. TUPLE WITH DICTIONARY (KEY-VALUE PAIRS)
# ============================================================================

print(f"\n--- Tuple Iteration ---")

students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78)
]

print("Student Scores:")
for name, score in students:
    print(f"  {name}: {score}")

# ============================================================================
# 11. PRACTICE PROBLEMS
# ============================================================================

print(f"\n--- Practice Problems ---")

# Problem 1: Tuple operations
print("\nProblem 1: Tuple Operations")
t1 = (1, 2, 3)
t2 = (4, 5, 6)
combined = t1 + t2
print(f"({t1} + {t2}) = {combined}")

# Problem 2: Find position
print("\nProblem 2: Find Element Position")
colors = ("red", "blue", "green", "yellow", "blue")
pos = colors.index("green")
print(f"Position of 'green': {pos}")

# Problem 3: Unpack and calculate
print("\nProblem 3: Unpack and Calculate")
point = (5, 12)
x, y = point
distance = (x**2 + y**2)**0.5
print(f"Distance from origin: {distance:.2f}")

# ============================================================================
# 12. CHALLENGES
# ============================================================================

print(f"\n--- Challenges ---")

# Challenge 1: Named tuples
print("\nChallenge 1: Create a simple struct-like tuple")
# TODO: Create tuple to represent a person (name, age, email)
# Access and print the values

# Challenge 2: Tuple sorting
print("\nChallenge 2: Sort tuples")
# TODO: Sort list of (name, grade) tuples by grade

# Challenge 3: Find duplicates
print("\nChallenge 3: Find Duplicate Positions")
# TODO: Find all positions of a specific element in a tuple
