# 57. Group Words by First Letter
# Input: ['cat', 'car', 'apple', 'bat']
# Output: {'c':['cat','car'], 'a':['apple'], 'b':['bat']}

lst = ['cat', 'car', 'apple', 'bat']
d = {}
for word in lst:
    first_letter = word[0]
    if first_letter in d:
        d[first_letter].append(word)
    else:
        d[first_letter] = [word]
print(d)

