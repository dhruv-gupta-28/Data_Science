#Product of alternate elements

# Read comma-separated numbers and convert to ints (ignore extra spaces)
n = int(input("Enter number of elements: "))
li = []
for i in range (n):
    ele = int(input("Enter element {}: ".format(i+1)))
    li.append(ele)
product = 1
for i in range(0, len(li), 2):
    product *= li[i]
print("The product of alternate elements is:", product)