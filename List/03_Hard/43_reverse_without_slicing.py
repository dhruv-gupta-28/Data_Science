# 43. Reverse without slicing or reverse()
# Input: [10, 20, 30, 40]
# Output: [40, 30, 20, 10]

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))
    lst.append(ele)

# Reverse manually
for i in range(len(lst) // 2):
    # Swap elements
    lst[i], lst[len(lst) - 1 - i] = lst[len(lst) - 1 - i], lst[i]

print(f"Reversed list: {lst}")

