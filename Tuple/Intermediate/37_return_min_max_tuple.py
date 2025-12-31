# 37. Return min and max from a tuple
# Input: (10, 20, 5, 15)
# Output: (5, 20)

t = (10, 20, 5, 15)

minimum = t[0]
maximum = t[0]

for num in t:
    if num < minimum:
        minimum = num
    if num > maximum:
        maximum = num

result = (minimum, maximum)
print(result)

