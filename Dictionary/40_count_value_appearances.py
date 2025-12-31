# 40. Count How Many Times a Value Appears
# Input: {'a': 1, 'b': 2, 'c': 1, 'd': 2, 'e': 1}
# Output: 1 appears 3 times

d = {'a': 1, 'b': 2, 'c': 1, 'd': 2, 'e': 1}
value_to_count = 1
count = 0
for v in d.values():
    if v == value_to_count:
        count += 1
print(f"{value_to_count} appears {count} times")

