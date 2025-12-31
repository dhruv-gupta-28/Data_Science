# 14. Find the index of an element in a tuple
# Input: (10, 20, 30, 40)
# Output: Index of 30 is 2

t = (10, 20, 30, 40)
element = 30

index = -1
for i in range(len(t)):
    if t[i] == element:
        index = i
        break

if index != -1:
    print(f"Index of {element} is {index}")
else:
    print(f"{element} not found")

