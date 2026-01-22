# 46. Dictionary of Squares using Comprehension
# Input: n = 5
# Output: {1:1, 2:4, 3:9, 4:16, 5:25}

n = 5
d = {i: i**2 for i in range(1, n+1)}
print(d)

