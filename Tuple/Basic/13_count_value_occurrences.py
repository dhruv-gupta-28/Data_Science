# 13. Count how many times a value appears in a tuple
# Input: (1, 2, 1, 1, 3)
# Output: 1 appears 3 times

t = (1, 2, 1, 1, 3)
value = 1

count = 0
for item in t:
    if item == value:
        count += 1

print(f"{value} appears {count} times")

