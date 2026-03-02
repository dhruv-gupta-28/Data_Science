"""
Python Fundamentals: String Operations
======================================

Topics Covered:
- String concatenation
- String formatting (f-strings, .format(), %)
- String methods (upper, lower, split, join, etc.)
- String indexing and slicing
- String manipulation
"""

# ============================================================================
# 1. STRING BASICS
# ============================================================================

# Creating strings
single_quote = 'Hello'
double_quote = "World"
triple_quote = '''Multi-line
string example'''

print(f"Single: {single_quote}")
print(f"Double: {double_quote}")

# ============================================================================
# 2. STRING CONCATENATION
# ============================================================================

first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(f"\nConcatenation: {full_name}")

# Using * to repeat strings
separator = "-" * 30
print(separator)

# ============================================================================
# 3. F-STRINGS (Modern Way)
# ============================================================================

age = 25
score = 95.5
name = "Alice"

# Basic f-string
print(f"\nName: {name}, Age: {age}")

# With expressions
print(f"Next year: {age + 1}")
print(f"Score rounded: {score:.1f}")

# ============================================================================
# 4. OTHER FORMATTING METHODS
# ============================================================================

# Using .format()
message = "Hello {}, you have {} messages".format(name, 5)
print(f"\n.format(): {message}")

# Using % formatting (old way)
old_style = "Name: %s, Age: %d" % (name, age)
print(f"% formatting: {old_style}")

# ============================================================================
# 5. STRING METHODS
# ============================================================================

text = "Hello World Python"

print(f"\n--- String Methods ---")
print(f"Original: {text}")
print(f"upper(): {text.upper()}")
print(f"lower(): {text.lower()}")
print(f"capitalize(): {text.capitalize()}")
print(f"title(): {text.title()}")

# String replacement
print(f"\nreplace('Python', 'Java'): {text.replace('Python', 'Java')}")

# Finding substrings
print(f"find('World'): {text.find('World')}")
print(f"count('l'): {text.count('l')}")

# Splitting and joining
words = text.split()
print(f"\nOriginal split: {words}")
joined = "-".join(words)
print(f"Joined with '-': {joined}")

# ============================================================================
# 6. STRING INDEXING AND SLICING
# ============================================================================

word = "Python"
print(f"\n--- Indexing and Slicing ---")
print(f"String: {word}")
print(f"Index 0: {word[0]}")    # P
print(f"Index -1: {word[-1]}")  # n
print(f"Slice [0:3]: {word[0:3]}")   # Pyt
print(f"Slice [2:5]: {word[2:5]}")   # tho
print(f"Slice [::2]: {word[::2]}")   # Pto (every 2nd char)
print(f"Slice [::-1]: {word[::-1]}")  # nohtyP (reversed)

# ============================================================================
# 7. CHECKING SUBSTRINGS
# ============================================================================

sentence = "Python is awesome"
print(f"\n--- Substring Check ---")
print(f"'Python' in sentence: {'Python' in sentence}")
print(f"'Java' in sentence: {'Java' in sentence}")
print(f"sentence.startswith('Python'): {sentence.startswith('Python')}")
print(f"sentence.endswith('awesome'): {sentence.endswith('awesome')}")

# ============================================================================
# 8. STRIPPING WHITESPACE
# ============================================================================

messy = "  Hello World  "
print(f"\n--- Whitespace Handling ---")
print(f"Original: '{messy}'")
print(f"strip(): '{messy.strip()}'")
print(f"lstrip(): '{messy.lstrip()}'")
print(f"rstrip(): '{messy.rstrip()}'")

# ============================================================================
# 9. PRACTICE PROBLEMS
# ============================================================================

print(f"\n--- Practice Problems ---")

# Problem 1: Full name from first and last name
print("\nProblem 1: Create Full Name")
first = "Jane"
last = "Smith"
full = f"{first} {last}"
print(f"Full name: {full}")

# Problem 2: Email formatting
print("\nProblem 2: Email Formatting")
email = "JOHN.DOE@EXAMPLE.COM"
email_lower = email.lower()
print(f"Original: {email}")
print(f"Formatted: {email_lower}")

# Problem 3: Count specific character
print("\nProblem 3: Character Count")
text = "Mississippi"
count = text.count('s')
print(f"Count of 's' in '{text}': {count}")

# Problem 4: Extract domain from email
print("\nProblem 4: Extract Domain")
email = "user@example.com"
domain = email.split('@')[1]
print(f"Email: {email}")
print(f"Domain: {domain}")

# ============================================================================
# 10. CHALLENGES
# ============================================================================

print("\n--- Challenges ---")

# Challenge 1: Reverse a string
print("\nChallenge 1: Reverse String")
# TODO: Take a string and reverse it without using slice [::-1]

# Challenge 2: Check palindrome
print("\nChallenge 2: Palindrome Check")
# TODO: Check if a string is a palindrome (reads same forwards/backwards)

# Challenge 3: Count words
print("\nChallenge 3: Word Count")
# TODO: Count number of words in a sentence

# Challenge 4: Remove vowels
print("\nChallenge 4: Remove Vowels")
# TODO: Remove all vowels from a string
