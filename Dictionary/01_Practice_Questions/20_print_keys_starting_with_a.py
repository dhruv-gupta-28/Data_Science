# 20. Print Keys Starting with 'a'
# Input: {'apple': 10, 'ball': 20, 'ant': 30}
# Output: apple, ant (each on new line)

d = {'apple': 10, 'ball': 20, 'ant': 30}
for key in d:
    if key.startswith('a'):
        print(key)

