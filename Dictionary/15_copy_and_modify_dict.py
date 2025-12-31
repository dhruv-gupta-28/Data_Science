# 15. Copy and Modify Dictionary
# Problem: Copy the dictionary and modify only the copy.
# Input: {'name': 'Anil', 'age': 18}
# Output: Original: {'name': 'Anil', 'age': 18}, Copy: {'name': 'Anil', 'age': 20}

original = {'name': 'Anil', 'age': 18}
copy_dict = original.copy()
copy_dict['age'] = 20
print(f"Original: {original}")
print(f"Copy: {copy_dict}")

