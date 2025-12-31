# 51. Find all pairs with given sum
# Input: [1, 2, 3, 4, 5], sum = 6
# Output: (1,5), (2,4)

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))
    lst.append(ele)

target_sum = int(input("Enter target sum: "))

pairs = []
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] + lst[j] == target_sum:
            pairs.append((lst[i], lst[j]))

print("Pairs with given sum:")
for pair in pairs:
    print(pair, end=" ")
print()

