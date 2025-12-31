# 24. Create a tuple from user input
# Input: Enter numbers: 1 2 3
# Output: (1, 2, 3)

user_input = input("Enter numbers separated by space: ")
numbers = user_input.split()
t = tuple(int(num) for num in numbers)
print(t)

