# 46. Remove empty tuples from a list
# Input: [(), (1,2), (), (3,4)]
# Output: [(1,2), (3,4)]

lst = [(), (1, 2), (), (3, 4)]

result_list = []
for item in lst:
    if len(item) > 0:
        result_list.append(item)

print(result_list)

