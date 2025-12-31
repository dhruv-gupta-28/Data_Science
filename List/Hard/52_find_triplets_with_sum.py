# 52. Find triplets with given sum
# Input: [1, 2, 3, 4, 5, 6], sum = 10
# Output: (1,3,6), (2,3,5), (1,4,5)

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))
    lst.append(ele)

target_sum = int(input("Enter target sum: "))

triplets = []
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        for k in range(j + 1, len(lst)):
            if lst[i] + lst[j] + lst[k] == target_sum:
                triplets.append((lst[i], lst[j], lst[k]))

print("Triplets with given sum:")
for triplet in triplets:
    print(triplet, end=" ")
print()

