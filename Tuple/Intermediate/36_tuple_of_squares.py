# 36. Tuple of squares (1–10)
# Input: range(1, 11)
# Output: (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

squares_list = []
for i in range(1, 11):
    squares_list.append(i ** 2)

result = tuple(squares_list)
print(result)

