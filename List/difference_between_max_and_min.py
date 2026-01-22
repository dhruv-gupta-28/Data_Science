"""
Difference between max and min
Input: [10, 5, 8, 20, 3]
Output: 17
"""

n = int(input ("Enter number of elements:"))
li = []
for i in range(n):
    ele = int(input())
    li.append(ele)
maxi = max(li)
mini = min(li)
diff = maxi - mini
print("Difference between max and min is:", diff)