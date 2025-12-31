# 29. Dictionary of Cubes
# Problem: Create a dictionary with numbers 1 to 5 as keys and their cubes as values.
# Output: {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}

d = {}
for i in range(1, 6):
    d[i] = i ** 3
print(d)

