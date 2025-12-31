# 39. Get every alternate element
# Input: (10, 20, 30, 40, 50)
# Output: (10, 30, 50)

t = (10, 20, 30, 40, 50)

alternate_list = []
for i in range(0, len(t), 2):
    alternate_list.append(t[i])

result = tuple(alternate_list)
print(result)

