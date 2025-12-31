# 54. Sort Dictionary by Values Descending
# Input: {'a':10, 'b':5, 'c':20}
# Output: {'c':20, 'a':10, 'b':5}

d = {'a': 10, 'b': 5, 'c': 20}
sorted_items = sorted(d.items(), key=lambda x: x[1], reverse=True)
result = {}
for key, value in sorted_items:
    result[key] = value
print(result)

