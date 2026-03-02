"""
Python Fundamentals: Data Structures - Strings
==============================================

Topics Covered:
- String basics and immutability
- Character access and indexing
- String methods (case, strip, replace, split, join)
- String formatting
- Checking string properties (isdigit, isalpha, etc.)
- Regular expressions basics
"""

# ============================================================================
# 1. STRING BASICS
# ============================================================================

print("--- String Basics ---")

# Creating strings
text = "Hello, Python!"
single_quote = 'String with single quotes'
multi_line = """This is a
multi-line
string"""

print(f"Text: {text}")
print(f"Length: {len(text)}")
print(f"Type: {type(text)}")

# Strings are immutable - cannot change characters
# text[0] = 'J'  # This would error!

# ============================================================================
# 2. STRING INDEXING AND SLICING
# ============================================================================

print(f"\n--- Indexing and Slicing ---")

word = "Programming"
print(f"String: {word}")
print(f"Index 0: {word[0]}")
print(f"Index -1: {word[-1]}")
print(f"Slice [0:7]: {word[0:7]}")
print(f"Slice [::2]: {word[::2]}")
print(f"Reversed: {word[::-1]}")

# ============================================================================
# 3. STRING CASE METHODS
# ============================================================================

print(f"\n--- Case Methods ---")

text = "Hello World Python"
print(f"original(): {text}")
print(f"upper(): {text.upper()}")
print(f"lower(): {text.lower()}")
print(f"title(): {text.title()}")
print(f"capitalize(): {text.capitalize()}")
print(f"swapcase(): {text.swapcase()}")

# ============================================================================
# 4. STRING SEARCH AND REPLACE
# ============================================================================

print(f"\n--- Search and Replace ---")

sentence = "The quick brown fox jumps"
print(f"Original: {sentence}")

# Find and count
print(f"find('quick'): {sentence.find('quick')}")
print(f"count('o'): {sentence.count('o')}")
print(f"startswith('The'): {sentence.startswith('The')}")
print(f"endswith('jumps'): {sentence.endswith('jumps')}")

# Replace
modified = sentence.replace("quick", "slow")
print(f"Replace: {modified}")

# ============================================================================
# 5. STRING WHITESPACE HANDLING
# ============================================================================

print(f"\n--- Whitespace Handling ---")

messy = "  Hello World  "
print(f"Original: '{messy}'")
print(f"strip(): '{messy.strip()}'")
print(f"lstrip(): '{messy.lstrip()}'")
print(f"rstrip(): '{messy.rstrip()}'")

# ============================================================================
# 6. SPLIT AND JOIN
# ============================================================================

print(f"\n--- Split and Join ---")

# Split string into list
text = "apple,banana,cherry,date"
fruits = text.split(",")
print(f"Split: {fruits}")

# Join list into string
words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print(f"Join: {sentence}")

# Split by whitespace
text = "One   Two    Three"
parts = text.split()
print(f"Split whitespace: {parts}")

# ============================================================================
# 7. STRING CHECKING METHODS
# ============================================================================

print(f"\n--- Checking Methods ---")

# Check character types
print(f"'123'.isdigit(): {'123'.isdigit()}")
print(f"'abc'.isalpha(): {'abc'.isalpha()}")
print(f"'abc123'.isalnum(): {'abc123'.isalnum()}")
print(f"'   '.isspace(): {'   '.isspace()}")
print(f"'Hello'.isupper(): {'Hello'.isupper()}")
print(f"'HELLO'.isupper(): {'HELLO'.isupper()}")

# ============================================================================
# 8. STRING FORMATTING (REVIEW)
# ============================================================================

print(f"\n--- String Formatting ---")

name = "Alice"
age = 25
score = 95.5

# F-strings
print(f"F-string: {name} is {age} years old")

# Format method
print("Format: {} is {} years old".format(name, age))

# % formatting
print("Percent: %s is %d years old" % (name, age))

# ============================================================================
# 9. STRING CONCATENATION AND REPETITION
# ============================================================================

print(f"\n--- Concatenation and Repetition ---")

# Concatenation
greeting = "Hello" + " " + "World"
print(f"Concatenation: {greeting}")

# Repetition
border = "-" * 30
print(f"Repetition: {border}")

# ============================================================================
# 10. SUBSTRING OPERATIONS
# ============================================================================

print(f"\n--- Substring Operations ---")

text = "Python Programming"
substring = "Program"

# Check if substring exists
print(f"'{substring}' in text: {substring in text}")

# Find index
index = text.find(substring)
print(f"Index of '{substring}': {index}")

# Extract positions
start = text.find("Prog")
end = start + len("Program")
extracted = text[start:end]
print(f"Extracted: {extracted}")

# ============================================================================
# 11. PRACTICE PROBLEMS
# ============================================================================

print(f"\n--- Practice Problems ---")

# Problem 1: Reverse string
print("\nProblem 1: Reverse String")
original = "Hello"
reversed_str = original[::-1]
print(f"Original: {original}")
print(f"Reversed: {reversed_str}")

# Problem 2: Palindrome check
print("\nProblem 2: Palindrome Check")
word = "racecar"
is_palindrome = word == word[::-1]
print(f"'{word}' is palindrome: {is_palindrome}")

# Problem 3: Count vowels
print("\nProblem 3: Count Vowels")
text = "Programming"
vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)
print(f"Vowels in '{text}': {count}")

# Problem 4: Extract numbers from string
print("\nProblem 4: Extract Numbers")
text = "I have 5 apples and 3 oranges"
numbers = [char for char in text if char.isdigit()]
print(f"Numbers in '{text}': {numbers}")

# ============================================================================
# 12. CHALLENGES
# ============================================================================

print(f"\n--- Challenges ---")

# Challenge 1: Check for balanced parentheses
print("\nChallenge 1: Balanced Parentheses")
# TODO: Check if string has balanced parentheses/brackets

# Challenge 2: Remove duplicate characters
print("\nChallenge 2: Remove Duplicates")
# TODO: Remove duplicate characters while keeping order

# Challenge 3: Anagram checker
print("\nChallenge 3: Anagram Checker")
# TODO: Check if two strings are anagrams
