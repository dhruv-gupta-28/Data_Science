# 60. Map A–Z to ASCII
# Input: (no input)
# Output: {'A':65, 'B':66, ..., 'Z':90}

d = {}
for i in range(ord('A'), ord('Z') + 1):
    d[chr(i)] = i
print(d)

