"""
File Handling: JSON and Structured Data
========================================

Topics Covered:
- JSON structure and syntax
- Reading and writing JSON
- JSON validation
- Working with nested JSON
- JSON vs Python objects
- Pretty printing
"""

import json
import os

# ============================================================================
# 1. JSON BASICS
# ============================================================================

print("--- JSON Basics ---")

# JSON data types
json_data = {
    "name": "John Doe",
    "age": 30,
    "email": "john@example.com",
    "active": True,
    "scores": [85, 90, 78],
    "address": None
}

# Convert to JSON string
json_string = json.dumps(json_data)
print(f"JSON string: {json_string}")

# Pretty print JSON
json_pretty = json.dumps(json_data, indent=2)
print(f"\nPretty JSON:\n{json_pretty}")

# ============================================================================
# 2. WRITE JSON TO FILE
# ============================================================================

print("\n--- Write JSON to File ---")

students = [
    {"id": 1, "name": "Alice", "grade": 85},
    {"id": 2, "name": "Bob", "grade": 92},
    {"id": 3, "name": "Charlie", "grade": 78}
]

# Write to file
json_file = "students.json"
with open(json_file, 'w') as f:
    json.dump(students, f, indent=2)

print(f"Written to {json_file}")

# ============================================================================
# 3. READ JSON FROM FILE
# ============================================================================

print("\n--- Read JSON from File ---")

with open(json_file, 'r') as f:
    loaded_students = json.load(f)

print("Loaded data:")
for student in loaded_students:
    print(f"  {student['name']}: {student['grade']}")

# ============================================================================
# 4. WORKING WITH NESTED JSON
# ============================================================================

print("\n--- Nested JSON ---")

nested_data = {
    "company": "TechCorp",
    "employees": [
        {
            "name": "Alice",
            "department": "Engineering",
            "projects": ["ProjectA", "ProjectB"],
            "address": {
                "city": "New York",
                "zip": "10001"
            }
        },
        {
            "name": "Bob",
            "department": "Sales",
            "projects": ["ProjectC"],
            "address": {
                "city": "Boston",
                "zip": "02101"
            }
        }
    ]
}

# Access nested data
print(f"Company: {nested_data['company']}")
print(f"First employee: {nested_data['employees'][0]['name']}")
print(f"First employee city: {nested_data['employees'][0]['address']['city']}")

# ============================================================================
# 5. JSON PARSING WITH ERROR HANDLING
# ============================================================================

print("\n--- JSON Parsing with Error Handling ---")

# Valid JSON
valid_json = '{"name": "John", "age": 30}'
try:
    data = json.loads(valid_json)
    print(f"Valid JSON parsed: {data}")
except json.JSONDecodeError as e:
    print(f"JSON error: {e}")

# Invalid JSON
invalid_json = '{"name": "John", "age": 30,}'  # Trailing comma
try:
    data = json.loads(invalid_json)
except json.JSONDecodeError as e:
    print(f"Invalid JSON error: {e}")

# ============================================================================
# 6. WORKING WITH JSON ARRAYS
# ============================================================================

print("\n--- JSON Arrays ---")

# Reading array from JSON
json_array_data = [
    {"id": 1, "product": "Laptop", "price": 999},
    {"id": 2, "product": "Mouse", "price": 25},
    {"id": 3, "product": "Keyboard", "price": 75}
]

# Write array to file
array_file = "products.json"
with open(array_file, 'w') as f:
    json.dump(json_array_data, f, indent=2)

# Read and process array
with open(array_file, 'r') as f:
    products = json.load(f)

print("Products:")
for product in products:
    print(f"  {product['product']}: ${product['price']}")

# ============================================================================
# 7. CUSTOM JSON ENCODER/DECODER
# ============================================================================

print("\n--- Custom JSON Encoding ---")

from datetime import datetime, date

class CustomEncoder(json.JSONEncoder):
    """Custom encoder for non-serializable objects"""
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        elif isinstance(obj, date):
            return obj.isoformat()
        return super().default(obj)

data_with_date = {
    "event": "Birthday",
    "date": datetime(2024, 3, 15, 18, 30),
    "attendees": 25
}

# Encode with custom encoder
json_with_date = json.dumps(data_with_date, cls=CustomEncoder, indent=2)
print(f"JSON with date:\n{json_with_date}")

# ============================================================================
# 8. MERGING JSON FILES
# ============================================================================

print("\n--- Merging JSON ---")

# Create two JSON files
data1 = [{"id": 1, "name": "Alice"}]
data2 = [{"id": 2, "name": "Bob"}]

file1 = "data1.json"
file2 = "data2.json"

with open(file1, 'w') as f:
    json.dump(data1, f)

with open(file2, 'w') as f:
    json.dump(data2, f)

# Merge them
merged_data = []
for filename in [file1, file2]:
    with open(filename, 'r') as f:
        data = json.load(f)
        merged_data.extend(data)

merged_file = "merged.json"
with open(merged_file, 'w') as f:
    json.dump(merged_data, f, indent=2)

print(f"Merged {file1} and {file2} into {merged_file}")
print(f"Merged content: {merged_data}")

# ============================================================================
# 9. QUERY JSON DATA
# ============================================================================

print("\n--- Query JSON Data ---")

def get_by_id(data, id_value):
    """Find item by ID in JSON array"""
    for item in data:
        if item.get('id') == id_value:
            return item
    return None

student_id = 2
found = get_by_id(loaded_students, student_id)
print(f"Found student with ID {student_id}: {found}")

# ============================================================================
# 10. STREAMING LARGE JSON FILES
# ============================================================================

print("\n--- Working with Large JSON ---")

# For very large JSON files, use streaming
large_data = {"records": [{"id": i, "value": i*2} for i in range(100)]}

large_file = "large.json"
with open(large_file, 'w') as f:
    json.dump(large_data, f)

# Read and process line by line (for actual streaming format)
print(f"Created {large_file} with {len(large_data['records'])} records")

# ============================================================================
# 11. PRACTICE PROBLEMS
# ============================================================================

print("\n--- Practice Problems ---")

# Problem 1: Flatten JSON
print("\nProblem 1: Flatten JSON")
def flatten_json(data, parent_key=''):
    """Flatten nested JSON"""
    items = []
    for k, v in data.items():
        new_key = f"{parent_key}.{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_json(v, new_key).items())
        else:
            items.append((new_key, v))
    return dict(items)

nested = {"a": {"b": 1, "c": 2}, "d": 3}
flattened = flatten_json(nested)
print(f"Flattened: {flattened}")

# Problem 2: Validate JSON schema
print("\nProblem 2: JSON Validation")
def validate_student(data):
    """Validate student JSON structure"""
    required_fields = {'name', 'age', 'email'}
    return required_fields.issubset(data.keys()) and isinstance(data['age'], int)

valid_student = {"name": "John", "age": 20, "email": "john@example.com"}
invalid_student = {"name": "Jane", "age": "20"}

print(f"Valid student: {validate_student(valid_student)}")
print(f"Invalid student: {validate_student(invalid_student)}")

# ============================================================================
# 12. CLEANUP
# ============================================================================

print("\n--- Cleanup ---")

files_to_remove = [json_file, array_file, file1, file2, merged_file, large_file]
for file in files_to_remove:
    if os.path.exists(file):
        os.remove(file)
        print(f"Removed {file}")
