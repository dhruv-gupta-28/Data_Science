# 7. Check if an element exists in a tuple
# Input: Tuple → (1, 2, 3, 4), Element → 3
# Output: Element Found

t = (1, 2, 3, 4)
element = 3

found = False
for item in t:
    if item == element:
        found = True
        break

if found:
    print("Element Found")
else:
    print("Element Not Found")

