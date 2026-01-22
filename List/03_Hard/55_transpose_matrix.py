# 55. Transpose a matrix (list of lists)
# Input: [[1, 2, 3], [4, 5, 6]]
# Output: [[1, 4], [2, 5], [3, 6]]

rows = int(input("Enter number of rows: "))
matrix = []
for i in range(rows):
    cols = int(input(f"Enter number of columns in row {i+1}: "))
    row = []
    for j in range(cols):
        ele = int(input(f"Enter element at [{i}][{j}]: "))
        row.append(ele)
    matrix.append(row)

# Find maximum columns
max_cols = 0
for row in matrix:
    if len(row) > max_cols:
        max_cols = len(row)

# Transpose
transposed = []
for j in range(max_cols):
    new_row = []
    for i in range(rows):
        if j < len(matrix[i]):
            new_row.append(matrix[i][j])
    transposed.append(new_row)

print("Transposed matrix:")
for row in transposed:
    print(row)

