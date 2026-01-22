# 30. Print Key–Value Pairs
# Input: {'x': 10, 'y': 20}
# Output: x -> 10, y -> 20 (each on new line)

d = {'x': 10, 'y': 20}
for key, value in d.items():
    print(f"{key} -> {value}")

