# 22. Swap two tuples
# Input: a = (1, 2) and b = (3, 4)
# Output: a = (3, 4), b = (1, 2)

a = (1, 2)
b = (3, 4)

a, b = b, a

print(f"a = {a}")
print(f"b = {b}")

