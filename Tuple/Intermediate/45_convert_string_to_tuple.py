# 45. Convert string into tuple of characters
# Input: "HELLO"
# Output: ('H', 'E', 'L', 'L', 'O')

s = "HELLO"

char_list = []
for char in s:
    char_list.append(char)

result = tuple(char_list)
print(result)

