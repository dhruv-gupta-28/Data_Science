# Strings Revision

"""
Strings are the collection of characters enclosed within single quotes, double quotes, or triple quotes in Python.
"""

# ============================================
# 1. Basic String Creation
# ============================================

a = "Amritsar"
print(a)
print(type(a))

# ============================================
# 2. Strings are Immutable
# ============================================

"""
Strings in Python are immutable, which means that once a string is created, it cannot be changed.

Why?
This immutability is designed to enhance performance and memory efficiency.
When a string is modified, a new string is created in memory rather than altering the existing one.
This allows Python to optimize memory usage and improve performance, especially when dealing with 
large strings or multiple string operations.
"""

a = "Amritsar"
# a[0] = "B"  # This will raise an error because strings are immutable
# TypeError: 'str' object does not support item assignment

# Instead, we create a new string
a = "Harsh"
print(a)

# ============================================
# 3. Length and Index
# ============================================

a = "Amritsar"
print(len(a))  # Length of the string
print(a[0])    # First character (index 0)
print(a[3])    # Character at index 3

# ============================================
# 4. String Slicing
# ============================================

"""
String slicing allows you to extract a portion of a string by specifying a start and end index.
The syntax for slicing is: string[start:end], where 'start' is the index to begin

Syntax:
string[start:end:step]
"""

a = "Amritsar"
print(a[0:5])   # Slicing from index 0 to 4 (5 is exclusive)
print(a[:5:2])  # From start to index 4, step of 2

# ============================================
# 5. Negative Indexing
# ============================================

"""
Negative indexing allows you to access characters from the end of the string.
The last character has an index of -1, the second last character has an index of -2, and so on.
"""

a = "Amritsar"
print(a[-1])        # Last character
print(a[-2:-7:-1])  # Negative slicing with step

# ============================================
# 6. Escape Sequences
# ============================================

"""
Escape sequences are special characters that are used to represent certain whitespace or 
control characters within a string.

Common escape sequences include:
\n : Newline
\t : Tab
\\ : Backslash
\' : Single Quote
\" : Double Quote
"""

print(" \"Hello \nWorld\"")
print("Hello\tWorld")      # Tab
print("This is a backslash: \\")
print('It\'s a beautiful day')

# ============================================
# 7. String Methods
# ============================================

"""
Python provides several built-in string methods that allow you to manipulate and work with strings.
"""

sample_string = " Hello, World! "

print(sample_string.lower())                    # Convert to lowercase
print(sample_string.upper())                    # Convert to uppercase
print(sample_string.strip())                   # Remove leading and trailing whitespace
print(sample_string.replace("World", "Python")) # Replace substring
print(sample_string.split(","))                 # Split string into a list

# Additional common string methods:
print(sample_string.capitalize())               # Capitalize first letter
print(sample_string.title())                    # Title case
print(sample_string.count("l"))                 # Count occurrences
print(sample_string.find("World"))              # Find index of substring
print(sample_string.startswith(" Hello"))       # Check if starts with
print(sample_string.endswith("! "))            # Check if ends with

# ============================================
# 8. String vs Strings
# ============================================

"""
String refers to a single sequence of characters, while Strings refers to multiple sequences of characters.
"""

# Example of String (singular):
single_string = "Hello, World!"
print(single_string)

# Example of Strings (plural):
multiple_strings = ["Hello, World!", 'Python is fun', """Triple quotes string"""]
for s in multiple_strings:
    print(s)

