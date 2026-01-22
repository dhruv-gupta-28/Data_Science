# 27. Use setdefault() to Insert Missing Key
# Problem: Use setdefault() to insert a key "country" with default value "India" if it doesn't exist.
# Input: {'name': 'Ravi'}
# Output: {'name': 'Ravi', 'country': 'India'}

d = {'name': 'Ravi'}
d.setdefault('country', 'India')
print(d)

