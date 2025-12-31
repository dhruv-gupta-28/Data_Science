# 40. Split a tuple into two halves
# Input: (1, 2, 3, 4, 5, 6)
# Output: (1, 2, 3) and (4, 5, 6)

t = (1, 2, 3, 4, 5, 6)

mid = len(t) // 2
first_half = t[:mid]
second_half = t[mid:]

print(f"First half: {first_half}")
print(f"Second half: {second_half}")

