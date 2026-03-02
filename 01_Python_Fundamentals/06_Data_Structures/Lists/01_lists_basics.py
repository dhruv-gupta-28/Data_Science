"""
Python Fundamentals: Data Structures - Lists
============================================

Topics Covered:
- Creating and initializing lists
- Accessing list elements
- List slicing
- List methods (append, extend, insert, remove, pop, sort, etc.)
- List comprehension
"""

# ============================================================================
# 1. CREATING LISTS
# ============================================================================

print("--- Creating Lists ---")

# Empty list
empty_list = []

# List with initial values
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True]

print(f"Numbers: {numbers}")
print(f"Fruits: {fruits}")
print(f"Mixed: {mixed}")

# ============================================================================
# 2. ACCESSING ELEMENTS
# ============================================================================

print(f"\n--- Accessing Elements ---")
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
print(f"Second number: {numbers[1]}")

# ============================================================================
# 3. LIST SLICING
# ============================================================================

print(f"\n--- List Slicing ---")
print(f"First 3 numbers: {numbers[0:3]}")
print(f"From index 1 to end: {numbers[1:]}")
print(f"Every 2nd number: {numbers[::2]}")
print(f"Reversed: {numbers[::-1]}")

# ============================================================================
# 4. LIST METHODS - ADDING ELEMENTS
# ============================================================================

print(f"\n--- Adding Elements ---")

my_list = [1, 2, 3]
print(f"Original: {my_list}")

my_list.append(4)
print(f"After append(4): {my_list}")

my_list.extend([5, 6, 7])
print(f"After extend([5,6,7]): {my_list}")

my_list.insert(0, 0)
print(f"After insert(0, 0): {my_list}")

# ============================================================================
# 5. LIST METHODS - REMOVING ELEMENTS
# ============================================================================

print(f"\n--- Removing Elements ---")

my_list = [1, 2, 3, 4, 5, 3]
print(f"Original: {my_list}")

my_list.remove(3)  # Removes first occurrence
print(f"After remove(3): {my_list}")

popped = my_list.pop()
print(f"After pop(): {my_list} (popped: {popped})")

popped = my_list.pop(0)  
print(f"After pop(0): {my_list} (popped: {popped})")

my_list.clear()
print(f"After clear(): {my_list}")

# ============================================================================
# 6. LIST METHODS - FINDING ELEMENTS
# ============================================================================

print(f"\n--- Finding Elements ---")

fruits = ["apple", "banana", "cherry", "banana"]
print(f"List: {fruits}")

index = fruits.index("banana")
print(f"Index of 'banana': {index}")

count = fruits.count("banana")
print(f"Count of 'banana': {count}")

print(f"'apple' in list: {'apple' in fruits}")
print(f"'grape' in list: {'grape' in fruits}")

# ============================================================================
# 7. LIST METHODS - SORTING
# ============================================================================

print(f"\n--- Sorting ---")

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original: {numbers}")

sorted_asc = sorted(numbers)
print(f"Sorted ascending: {sorted_asc}")

sorted_desc = sorted(numbers, reverse=True)
print(f"Sorted descending: {sorted_desc}")

# In-place sorting
numbers.sort()
print(f"After .sort(): {numbers}")

# ============================================================================
# 8. LIST COMPREHENSION
# ============================================================================

print(f"\n--- List Comprehension ---")

# Simple comprehension
squares = [x**2 for x in range(1, 6)]
print(f"Squares 1-5: {squares}")

# With condition
evens = [x for x in range(1, 11) if x % 2 == 0]
print(f"Even numbers 1-10: {evens}")

# String operations
words = ["hello", "world", "python"]
uppercase = [word.upper() for word in words]
print(f"Uppercase: {uppercase}")

# ============================================================================
# 9. NESTED LISTS (MATRICES)
# ============================================================================

print(f"\n--- Nested Lists ---")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(f"Matrix:")
for row in matrix:
    print(row)

print(f"Element [1][2]: {matrix[1][2]}")
print(f"First row: {matrix[0]}")

# ============================================================================
# 10. ENUMERATION
# ============================================================================

print(f"\n--- Enumeration ---")

colors = ["red", "green", "blue"]
for i, color in enumerate(colors):
    print(f"{i}: {color}")

# With start index
for i, color in enumerate(colors, start=1):
    print(f"{i}: {color}")

# ============================================================================
# 11. PRACTICE PROBLEMS
# ============================================================================

print(f"\n--- Practice Problems ---")

# Problem 1: Sum of list
print("\nProblem 1: Sum of numbers")
nums = [10, 20, 30, 40, 50]
total = sum(nums)
print(f"List: {nums}, Sum: {total}")

# Problem 2: Find max and min
print("\nProblem 2: Max and Min")
nums = [45, 23, 67, 12, 89, 34]
print(f"List: {nums}")
print(f"Max: {max(nums)}, Min: {min(nums)}")

# Problem 3: Duplicate elements
print("\nProblem 3: Find duplicates")
items = [1, 2, 2, 3, 4, 4, 4, 5]
duplicates = [x for x in set(items) if items.count(x) > 1]
print(f"List: {items}")
print(f"Duplicates: {duplicates}")

# ============================================================================
# 12. CHALLENGES
# ============================================================================

print(f"\n--- Challenges ---")

# Challenge 1: Reverse list
print("\nChallenge 1: Reverse List")
# TODO: Reverse a list without using reverse() or [::-1]

# Challenge 2: Remove duplicates
print("\nChallenge 2: Remove Duplicates")
# TODO: Remove duplicate elements while preserving order

# Challenge 3: Flatten nested list
print("\nChallenge 3: Flatten Nested List")
# TODO: Convert nested list to flat list
