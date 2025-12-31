# 48. Multiply tuples element-wise
# Input: [(1,2), (3,4)]
# Output: (3, 8)

lst = [(1, 2), (3, 4)]

product_list = []
for pair in lst:
    product_list.append(pair[0] * pair[1])

result = tuple(product_list)
print(result)

