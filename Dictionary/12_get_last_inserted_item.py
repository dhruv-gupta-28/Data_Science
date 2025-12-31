# 12. Get Last Inserted Item
# Problem: Print the last inserted key-value pair.
# Input: {'x': 1, 'y': 2, 'z': 3}
# Output: ('z', 3)

d = {'x': 1, 'y': 2, 'z': 3}
# In Python 3.7+, dictionaries maintain insertion order
last_key = list(d.keys())[-1]
print((last_key, d[last_key]))

