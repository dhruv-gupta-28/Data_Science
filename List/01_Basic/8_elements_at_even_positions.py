# 8. Print elements at even positions
# Input: [10, 20, 30, 40, 50]
# Output: 10, 30, 50

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))
    lst.append(ele)

print("Elements at even positions (0-indexed):")
for i in range(len(lst)):
    if i % 2 == 0:
        print(lst[i])

