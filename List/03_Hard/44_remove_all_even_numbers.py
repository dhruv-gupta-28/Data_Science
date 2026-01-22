# 44. Remove all even numbers
# Input: [1, 2, 3, 4, 5, 6]
# Output: [1, 3, 5]

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))
    lst.append(ele)

result = []
for num in lst:
    if num % 2 != 0:
        result.append(num)

print(f"List after removing even numbers: {result}")

