# 17. Add 10 to each element
# Input: [1, 2, 3, 4]
# Output: [11, 12, 13, 14]

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))
    lst.append(ele)

result = []
for num in lst:
    result.append(num + 10)

print(f"Original list: {lst}")
print(f"After adding 10: {result}")

