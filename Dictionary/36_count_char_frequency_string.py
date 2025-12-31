# 36. Count Character Frequency in String
# Input: "banana"
# Output: {'b': 1, 'a': 3, 'n': 2}

s = "banana"
d = {}
for char in s:
    if char in d:
        d[char] += 1
    else:
        d[char] = 1
print(d)

