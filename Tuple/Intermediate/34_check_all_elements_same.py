# 34. Check if all elements are the same
# Input: (5, 5, 5, 5)
# Output: True

t = (5, 5, 5, 5)

if len(t) == 0:
    result = True
else:
    first = t[0]
    result = True
    for element in t:
        if element != first:
            result = False
            break

print(result)

