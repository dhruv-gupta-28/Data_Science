# 30. Filter out even numbers
# Input: (1, 2, 3, 4, 5, 6)
# Output: (1, 3, 5)

t = (1, 2, 3, 4, 5, 6)

odd_list = []
for num in t:
    if num % 2 != 0:
        odd_list.append(num)

result = tuple(odd_list)
print(result)

