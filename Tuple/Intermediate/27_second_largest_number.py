# 27. Get the second largest number
# Input: (10, 30, 20, 50, 40)
# Output: 40

t = (10, 30, 20, 50, 40)

# Find maximum
maximum = t[0]
for num in t:
    if num > maximum:
        maximum = num

# Find second largest
second_largest = None
for num in t:
    if num != maximum:
        if second_largest is None or num > second_largest:
            second_largest = num

print(second_largest)

