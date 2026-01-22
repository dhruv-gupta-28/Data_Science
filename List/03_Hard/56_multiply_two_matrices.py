# 56. Multiply two matrices
# Input: A = [[1,2],[3,4]], B = [[2,0],[1,2]]
# Output: [[4,4],[10,8]]

print("Matrix A:")
rows_a = int(input("Enter number of rows: "))
matrix_a = []
for i in range(rows_a):
    cols = int(input(f"Enter number of columns in row {i+1}: "))
    row = []
    for j in range(cols):
        ele = int(input(f"Enter element at [{i}][{j}]: "))
        row.append(ele)
    matrix_a.append(row)

print("Matrix B:")
rows_b = int(input("Enter number of rows: "))
matrix_b = []
for i in range(rows_b):
    cols = int(input(f"Enter number of columns in row {i+1}: "))
    row = []
    for j in range(cols):
        ele = int(input(f"Enter element at [{i}][{j}]: "))
        row.append(ele)
    matrix_b.append(row)

# Check if multiplication is possible
if len(matrix_a[0]) != len(matrix_b):
    print("Matrix multiplication not possible!")
else:
    # Initialize result matrix
    result = []
    for i in range(len(matrix_a)):
        result_row = []
        for j in range(len(matrix_b[0])):
            sum_val = 0
            for k in range(len(matrix_b)):
                sum_val += matrix_a[i][k] * matrix_b[k][j]
            result_row.append(sum_val)
        result.append(result_row)
    
    print("Result of matrix multiplication:")
    for row in result:
        print(row)

