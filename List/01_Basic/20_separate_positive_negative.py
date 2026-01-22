# 20. Separate positive and negative
# Input: [5, -2, 9, -4, 7]
# Output: Positive: [5, 9, 7], Negative: [-2, -4]

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))
    lst.append(ele)

positive = []
negative = []

for num in lst:
    if num > 0:
        positive.append(num)
    elif num < 0:
        negative.append(num)

print(f"Positive: {positive}")
print(f"Negative: {negative}")

