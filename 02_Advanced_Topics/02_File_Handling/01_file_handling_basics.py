"""
Advanced Topics: File Handling
==============================

Topics Covered:
- Opening and closing files
- Reading files (read, readline, readlines)
- Writing to files (write, writelines)
- Appending to files
- Working with different file types (txt, csv, json)
- File operations (exists, delete, rename)
- Error handling with files
- Context managers (with statement)
"""

import os
import json
import csv
from pathlib import Path

# ============================================================================
# 1. FILE BASICS
# ============================================================================

print("--- File Basics ---")

# Reading a file
filename = "example.txt"

# Create a sample file first
with open(filename, 'w') as f:
    f.write("Line 1: Hello\n")
    f.write("Line 2: File handling\n")
    f.write("Line 3: Python\n")

# Read entire file
with open(filename, 'r') as f:
    content = f.read()
    print("Using read():")
    print(content)

# ============================================================================
# 2. READING FILES - DIFFERENT METHODS
# ============================================================================

print("\n--- Reading Files ---")

# Method 1: read() - Read entire file as string
print("\nMethod 1: read()")
with open(filename, 'r') as f:
    content = f.read()
    print(f"Type: {type(content)}")
    print(f"Content: {repr(content)}")

# Method 2: readline() - Read one line at a time
print("\nMethod 2: readline()")
with open(filename, 'r') as f:
    line1 = f.readline()
    line2 = f.readline()
    print(f"First line: {repr(line1)}")
    print(f"Second line: {repr(line2)}")

# Method 3: readlines() - Read all lines as list
print("\nMethod 3: readlines()")
with open(filename, 'r') as f:
    lines = f.readlines()
    print(f"Type: {type(lines)}")
    print(f"Lines: {lines}")

# Me Method 4: Loop through file
print("\nMethod 4: Loop through file")
with open(filename, 'r') as f:
    for line in f:
        print(f"  {line.strip()}")

# ============================================================================
# 3. WRITING TO FILES
# ============================================================================

print("\n--- Writing to Files ---")

# Write mode ('w') - overwrites existing file
output_file = "output.txt"
with open(output_file, 'w') as f:
    f.write("First line\n")
    f.write("Second line\n")
    f.write("Third line\n")

print(f"Created {output_file}")

# Multiple writes
with open(output_file, 'w') as f:
    lines = ["Apple\n", "Banana\n", "Cherry\n"]
    f.writelines(lines)

print("File updated with fruits")

# ============================================================================
# 4. APPENDING TO FILES
# ============================================================================

print("\n--- Appending to Files ---")

# Append mode ('a') - adds to end of file
with open(output_file, 'a') as f:
    f.write("Date\n")
    f.write("Elderberry\n")

print("Appended more fruits")

with open(output_file, 'r') as f:
    print("Current content:")
    print(f.read())

# ============================================================================
# 5. FILE MODES
# ============================================================================

print("\n--- File Modes ---")

"""
'r'  - Read (default, file must exist)
'w'  - Write (creates file or overwrites)
'a'  - Append (creates file if doesn't exist)
'x'  - Exclusive creation (fails if file exists)
'b'  - Binary mode (use with r, w, a, x)
't'  - Text mode (default)
'+'  - Read and write
"""

# Example: 'x' mode - exclusive creation
try:
    with open("new_file.txt", 'x') as f:
        f.write("New exclusive file")
    print("Created new_file.txt exclusively")
except FileExistsError:
    print("File already exists")

# ============================================================================
# 6. WORKING WITH JSON
# ============================================================================

print("\n--- Working with JSON ---")

# Data to write
data = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "gaming", "coding"]
}

# Write to JSON file
json_file = "data.json"
with open(json_file, 'w') as f:
    json.dump(data, f, indent=4)

print(f"Wrote {json_file}")

# Read from JSON file
with open(json_file, 'r') as f:
    loaded_data = json.load(f)
    print(f"Loaded data: {loaded_data}")

# Pretty print
json_string = json.dumps(data, indent=2)
print("\nJSON string:")
print(json_string)

# ============================================================================
# 7. WORKING WITH CSV
# ============================================================================

print("\n--- Working with CSV ---")

# Write CSV
csv_file = "students.csv"
with open(csv_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Age', 'Grade'])
    writer.writerow(['Alice', 20, 'A'])
    writer.writerow(['Bob', 19, 'B'])
    writer.writerow(['Charlie', 21, 'A+'])

print(f"Wrote {csv_file}")

# Read CSV
print("\nReading CSV:")
with open(csv_file, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Read as dictionaries
print("\nReading CSV as dictionaries:")
with open(csv_file, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(dict(row))

# ============================================================================
# 8. FILE OPERATIONS
# ============================================================================

print("\n--- File Operations ---")

# Check if file exists
if os.path.exists("example.txt"):
    print("example.txt exists")

# Get file size
size = os.path.getsize("example.txt")
print(f"File size: {size} bytes")

# Get file info
stat_info = os.stat("example.txt")
print(f"File created: {stat_info.st_ctime}")

# ============================================================================
# 9. ERROR HANDLING WITH FILES
# ============================================================================

print("\n--- Error Handling ---")

try:
    with open("nonexistent.txt", 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("File not found!")
except IOError as e:
    print(f"IO error: {e}")

# ============================================================================
# 10. WORKING WITH DIRECTORIES
# ============================================================================

print("\n--- Working with Directories ---")

# Current directory
current_dir = os.getcwd()
print(f"Current directory: {current_dir}")

# List files in directory
print("\nFiles in current directory:")
for file in os.listdir("."):
    if os.path.isfile(file):
        print(f"  {file}")

# Create directory
if not os.path.exists("test_folder"):
    os.makedirs("test_folder")
    print("Created test_folder")

# ============================================================================
# 11. USING PATHLIB (MODERN APPROACH)
# ============================================================================

print("\n--- Using pathlib ---")

# Create Path object
file_path = Path("example.txt")

# Check existence
print(f"Exists: {file_path.exists()}")

# Get file name
print(f"Name: {file_path.name}")

# Get parent directory
print(f"Parent: {file_path.parent}")

# Absolute path
print(f"Absolute: {file_path.absolute()}")

# Read file using Path
content = file_path.read_text()
print(f"Content: {repr(content[:30])}...")

# ============================================================================
# 12. CONTEXT MANAGERS (WITH STATEMENT)
# ============================================================================

print("\n--- Context Managers ---")

"""
The 'with' statement is a context manager that:
- Automatically opens the file
- Ensures it's closed even if error occurs
- Cleans up resources properly
"""

# Without context manager (old way)
# f = open("file.txt", 'r')
# content = f.read()
# f.close()

# With context manager (modern way)
with open("example.txt", 'r') as f:
    content = f.read()
print("File automatically closed after 'with' block")

# ============================================================================
# 13. PRACTICE PROBLEMS
# ============================================================================

print("\n--- Practice Problems ---")

# Problem 1: Count lines in file
print("\nProblem 1: Count Lines")
def count_lines(filename):
    """Count number of lines in a file"""
    with open(filename, 'r') as f:
        return len(f.readlines())

line_count = count_lines("example.txt")
print(f"Lines in example.txt: {line_count}")

# Problem 2: Copy file
print("\nProblem 2: Copy File")
def copy_file(source, destination):
    """Copy file from source to destination"""
    with open(source, 'r') as f:
        content = f.read()
    with open(destination, 'w') as f:
        f.write(content)

copy_file("example.txt", "example_copy.txt")
print("Copied example.txt to example_copy.txt")

# ============================================================================
# 14. CHALLENGES
# ============================================================================

print("\n--- Challenges ---")

# Challenge 1: Word frequency counter
print("\nChallenge 1: Word Frequency")
# TODO: Read a file and count frequency of each word

# Challenge 2: Merge multiple files
print("\nChallenge 2: Merge Files")
# TODO: Merge content of multiple text files into one

# Challenge 3: JSON to CSV converter
print("\nChallenge 3: JSON to CSV")
# TODO: Convert JSON file to CSV format

# ============================================================================
# 15. CLEANUP
# ============================================================================

print("\n--- Cleanup ---")

# Clean up test files
files_to_remove = [filename, output_file, json_file, csv_file, "example_copy.txt", "new_file.txt"]
for file in files_to_remove:
    if os.path.exists(file):
        os.remove(file)
        print(f"Removed {file}")

# Remove test folder
if os.path.exists("test_folder"):
    os.rmdir("test_folder")
    print("Removed test_folder")
