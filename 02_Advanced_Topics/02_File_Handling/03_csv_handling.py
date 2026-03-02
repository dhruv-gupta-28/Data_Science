"""
File Handling: CSV and Data Files
==================================

Topics Covered:
- CSV format and structure
- Reading CSV files
- Writing CSV files
- CSV with headers
- Processing CSV data
- CSV to dictionary/list conversion
- Filtering and transforming CSV
"""

import csv
import os

# ============================================================================
# 1. CSV BASICS
# ============================================================================

print("--- CSV Basics ---")

# Create a simple CSV file
csv_file = "data.csv"
with open(csv_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['Alice', 25, 'New York'])
    writer.writerow(['Bob', 30, 'Boston'])
    writer.writerow(['Charlie', 28, 'Chicago'])

print(f"Created {csv_file}")

# ============================================================================
# 2. READ CSV - BASIC METHOD
# ============================================================================

print("\n--- Read CSV (Basic) ---")

with open(csv_file, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# ============================================================================
# 3. READ CSV - AS DICTIONARIES
# ============================================================================

print("\n--- Read CSV as Dictionaries ---")

with open(csv_file, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(dict(row))

# ============================================================================
# 4. WRITE CSV - BASIC METHOD
# ============================================================================

print("\n--- Write CSV (Basic) ---")

output_file = "output.csv"
with open(output_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Product', 'Price', 'Quantity'])
    writer.writerow(['Laptop', 999, 5])
    writer.writerow(['Mouse', 25, 50])
    writer.writerow(['Keyboard', 75, 30])

print(f"Created {output_file}")

# ============================================================================
# 5. WRITE CSV - USING DICTWRITER
# ============================================================================

print("\n--- Write CSV with DictWriter ---")

students_file = "students.csv"
students = [
    {'id': 1, 'name': 'Alice', 'grade': 85},
    {'id': 2, 'name': 'Bob', 'grade': 92},
    {'id': 3, 'name': 'Charlie', 'grade': 78}
]

with open(students_file, 'w', newline='') as f:
    fieldnames = ['id', 'name', 'grade']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students)

print(f"Created {students_file}")

# ============================================================================
# 6. FILTER CSV DATA
# ============================================================================

print("\n--- Filter CSV Data ---")

# Find rows where age > 25
print("People older than 25:")
with open(csv_file, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        age = int(row['Age'])
        if age > 25:
            print(f"  {row['Name']}: {age}")

# ============================================================================
# 7. TRANSFORM CSV DATA
# ============================================================================

print("\n--- Transform CSV Data ---")

# Add computed column
transformed_file = "transformed.csv"
with open(csv_file, 'r') as infile, open(transformed_file, 'w', newline='') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames + ['Age Group']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for row in reader:
        age = int(row['Age'])
        row['Age Group'] = 'Young' if age < 30 else 'Mature'
        writer.writerow(row)

print(f"Created {transformed_file} with computed column")

# ============================================================================
# 8. CSV TO DICTIONARY/LIST
# ============================================================================

print("\n--- CSV to Data Structures ---")

# CSV to list of dictionaries
def csv_to_list(filename):
    """Read CSV and return list of dictionaries"""
    data = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    return data

data = csv_to_list(csv_file)
print(f"CSV as list of dicts: {data}")

# CSV to list of lists
def csv_to_lists(filename):
    """Read CSV and return list of lists"""
    data = []
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data

lists = csv_to_lists(csv_file)
print(f"CSV as list of lists: {lists}")

# ============================================================================
# 9. MERGE MULTIPLE CSV FILES
# ============================================================================

print("\n--- Merge CSV Files ---")

# Create two CSV files to merge
file1 = "file1.csv"
file2 = "file2.csv"

with open(file1, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['ID', 'Name'])
    writer.writerow([1, 'Alice'])
    writer.writerow([2, 'Bob'])

with open(file2, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['ID', 'Name'])
    writer.writerow([3, 'Charlie'])
    writer.writerow([4, 'Diana'])

# Merge them
merged_file = "merged.csv"
with open(merged_file, 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['ID', 'Name'])  # Header
    
    for infile in [file1, file2]:
        with open(infile, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip header
            for row in reader:
                writer.writerow(row)

print(f"Merged {file1} and {file2} into {merged_file}")

# ============================================================================
# 10. CSV WITH SPECIAL CHARACTERS
# ============================================================================

print("\n--- CSV with Special Characters ---")

special_file = "special.csv"
with open(special_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Description', 'Price'])
    writer.writerow(['Product A', 'Description with, comma', 100])
    writer.writerow(['Product B', 'Description with "quotes"', 200])
    writer.writerow(['Product C', 'Multi\nline\ntext', 300])

print(f"Created {special_file} with special characters")

# Read and verify
with open(special_file, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# ============================================================================
# 11. PRACTICE PROBLEMS
# ============================================================================

print("\n--- Practice Problems ---")

# Problem 1: Calculate statistics
print("\nProblem 1: CSV Statistics")
def csv_statistics(filename, numeric_column):
    """Calculate stats for numeric column"""
    values = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            values.append(float(row[numeric_column]))
    
    return {
        'min': min(values),
        'max': max(values),
        'avg': sum(values) / len(values),
        'count': len(values)
    }

stats = csv_statistics(csv_file, 'Age')
print(f"Age statistics: {stats}")

# Problem 2: Group by column
print("\nProblem 2: Group CSV by Column")
def group_by(filename, group_column):
    """Group CSV rows by column value"""
    groups = {}
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            key = row[group_column]
            if key not in groups:
                groups[key] = []
            groups[key].append(row)
    return groups

# Create sample data with city
city_file = "cities.csv"
with open(city_file, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['Name', 'City', 'Age'])
    writer.writeheader()
    writer.writerows([
        {'Name': 'Alice', 'City': 'NYC', 'Age': '25'},
        {'Name': 'Bob', 'City': 'Boston', 'Age': '30'},
        {'Name': 'Charlie', 'City': 'NYC', 'Age': '28'}
    ])

groups = group_by(city_file, 'City')
for city, people in groups.items():
    print(f"  {city}: {[p['Name'] for p in people]}")

# ============================================================================
# 12. CLEANUP
# ============================================================================

print("\n--- Cleanup ---")

files_to_remove = [csv_file, output_file, students_file, transformed_file,
                   file1, file2, merged_file, special_file, city_file]
for file in files_to_remove:
    if os.path.exists(file):
        os.remove(file)
        print(f"Removed {file}")
