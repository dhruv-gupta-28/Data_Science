"""
Python Fundamentals: Data Structures - Dictionaries
===================================================

Topics Covered:
- Creating dictionaries
- Accessing values
- Adding/updating items
- Dictionary methods (keys, values, items, get, pop, etc.)
- Dictionary comprehension
- Nested dictionaries
"""

# ============================================================================
# 1. CREATING DICTIONARIES
# ============================================================================

print("--- Creating Dictionaries ---")

# Empty dictionary
empty_dict = {}

# Dictionary with initial values
student = {
    "name": "Alice",
    "age": 20,
    "gpa": 3.8
}

person = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 30,
    "address": "123 Main St"
}

print(f"Student: {student}")
print(f"Person: {person}")

# ============================================================================
# 2. ACCESSING VALUES
# ============================================================================

print(f"\n--- Accessing Values ---")

print(f"Student name: {student['name']}")
print(f"Student age: {student['age']}")

# Using get() method (safer)
gpa = student.get('gpa')
print(f"GPA: {gpa}")

# Default value if key not found
major = student.get('major', 'Not specified')
print(f"Major: {major}")

# ============================================================================
# 3. ADDING AND UPDATING ITEMS
# ============================================================================

print(f"\n--- Adding and Updating Items ---")

student['major'] = 'Computer Science'
print(f"After adding major: {student}")

student['age'] = 21
print(f"After updating age: {student}")

student.update({'gpa': 3.9, 'year': 3})
print(f"After bulk update: {student}")

# ============================================================================
# 4. REMOVING ITEMS
# ============================================================================

print(f"\n--- Removing Items ---")

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(f"Original: {my_dict}")

del my_dict['a']
print(f"After del my_dict['a']: {my_dict}")

popped = my_dict.pop('b')
print(f"After pop('b'): {my_dict} (popped: {popped})")

# ============================================================================
# 5. DICTIONARY METHODS
# ============================================================================

print(f"\n--- Dictionary Methods ---")

book = {
    "title": "Python 101",
    "author": "John Smith",
    "year": 2023,
    "pages": 450
}

print(f"Keys: {book.keys()}")
print(f"Values: {book.values()}")
print(f"Items: {book.items()}")

# Check if key exists
print(f"'author' in book: {'author' in book}")
print(f"'publisher' in book: {'publisher' in book}")

# Get length
print(f"Number of items: {len(book)}")

# ============================================================================
# 6. ITERATING DICTIONARIES
# ============================================================================

print(f"\n--- Iterating Dictionaries ---")

scores = {"Alice": 85, "Bob": 92, "Charlie": 78}

print("Iterating keys:")
for name in scores:
    print(f"  {name}: {scores[name]}")

print("\nIterating items:")
for name, score in scores.items():
    print(f"  {name}: {score}")

# ============================================================================
# 7. DICTIONARY COMPREHENSION
# ============================================================================

print(f"\n--- Dictionary Comprehension ---")

# Simple comprehension
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

# With condition
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# From existing dict
prices = {'apple': 1.5, 'banana': 0.75, 'orange': 2.0}
discounted = {item: price * 0.9 for item, price in prices.items()}
print(f"Original: {prices}")
print(f"10% discount: {discounted}")

# ============================================================================
# 8. NESTED DICTIONARIES
# ============================================================================

print(f"\n--- Nested Dictionaries ---")

company = {
    "name": "TechCorp",
    "employees": {
        "emp1": {"name": "Alice", "department": "Engineering"},
        "emp2": {"name": "Bob", "department": "Sales"},
        "emp3": {"name": "Charlie", "department": "Marketing"}
    }
}

print(f"Company: {company['name']}")
print(f"First employee: {company['employees']['emp1']}")
print(f"emp2 department: {company['employees']['emp2']['department']}")

# ============================================================================
# 9. MERGING DICTIONARIES
# ============================================================================

print(f"\n--- Merging Dictionaries ---")

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged = {**dict1, **dict2}
print(f"Merged: {merged}")

# Update method
dict1.update(dict2)
print(f"After update: {dict1}")

# ============================================================================
# 10. PRACTICE PROBLEMS
# ============================================================================

print(f"\n--- Practice Problems ---")

# Problem 1: Count word frequency
print("\nProblem 1: Word Frequency")
text = "hello world hello python world python python"
words = text.split()
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1
print(f"Text: {text}")
print(f"Frequency: {frequency}")

# Problem 2: Find richest person
print("\nProblem 2: Find Richest")
bank_accounts = {
    "Alice": 5000,
    "Bob": 3000,
    "Charlie": 7500
}
richest = max(bank_accounts, key=bank_accounts.get)
print(f"Accounts: {bank_accounts}")
print(f"Richest: {richest} (${bank_accounts[richest]})")

# Problem 3: Invert dictionary
print("\nProblem 3: Invert Dictionary")
mapping = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in mapping.items()}
print(f"Original: {mapping}")
print(f"Inverted: {inverted}")

# ============================================================================
# 11. CHALLENGES
# ============================================================================

print(f"\n--- Challenges ---")

# Challenge 1: Two sum
print("\nChallenge 1: Two Sum")
# TODO: Find two numbers in dictionary that sum to target

# Challenge 2: Anagram checker
print("\nChallenge 2: Anagram Checker")
# TODO: Check if words are anagrams using character frequency

# Challenge 3: Group by key
print("\nChallenge 3: Group Items")
# TODO: Group a list of dicts by a specific key value
