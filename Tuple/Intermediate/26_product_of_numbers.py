# 26. Find the product of all numbers in a tuple
# Input: (2, 3, 4)
# Output: 24

t = (2, 3, 4)

product = 1
for num in t:
    product *= num

print(product)

