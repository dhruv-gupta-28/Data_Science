# 24. Print key: value Format
# Input: {'name': 'Rita', 'age': 19}
# Output: name: Rita, age: 19 (each on new line)

d = {'name': 'Rita', 'age': 19}
for key, value in d.items():
    print(f"{key}: {value}")

