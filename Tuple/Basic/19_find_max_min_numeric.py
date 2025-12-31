# 19. Find maximum and minimum value in a numeric tuple
# Input: (5, 1, 9, 3)
# Output: Max: 9, Min: 1

t = (5, 1, 9, 3)

maximum = t[0]
minimum = t[0]

for num in t:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num

print(f"Max: {maximum}")
print(f"Min: {minimum}")

