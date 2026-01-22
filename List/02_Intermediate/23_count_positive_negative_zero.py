# 23. Count positive, negative, and zero elements
# Input: [2, -3, 0, 4, -1]
# Output: Positive: 2, Negative: 2, Zero: 1

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))
    lst.append(ele)

positive_count = 0
negative_count = 0
zero_count = 0

for num in lst:
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    else:
        zero_count += 1

print(f"Positive: {positive_count}")
print(f"Negative: {negative_count}")
print(f"Zero: {zero_count}")

