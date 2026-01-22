# 34. Difference between max and min
# Input: [10, 5, 8, 20, 3]
# Output: 17

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))
    lst.append(ele)

maximum = lst[0]
minimum = lst[0]

for num in lst:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num

difference = maximum - minimum
print(f"Difference between max and min: {difference}")

