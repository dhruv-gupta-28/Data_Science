# 58. Multiples Dictionary
# Input: Numbers 1–3
# Output: {1:[1,2,3,4,5], 2:[2,4,6,8,10], 3:[3,6,9,12,15]}

d = {}
for i in range(1, 4):
    multiples = []
    for j in range(1, 6):
        multiples.append(i * j)
    d[i] = multiples
print(d)

