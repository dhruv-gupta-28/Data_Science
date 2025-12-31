# 29. Convert a tuple of tuples into a dictionary
# Input: (("a", 1), ("b", 2))
# Output: {'a': 1, 'b': 2}

t = (("a", 1), ("b", 2))

d = {}
for pair in t:
    d[pair[0]] = pair[1]

print(d)

