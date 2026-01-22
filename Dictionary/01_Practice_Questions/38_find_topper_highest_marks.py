# 38. Find Topper (Highest Marks)
# Input: {'Amit': 85, 'Riya': 92, 'Sohan': 78}
# Output: Topper: Riya

d = {'Amit': 85, 'Riya': 92, 'Sohan': 78}
max_marks = max(d.values())
for name, marks in d.items():
    if marks == max_marks:
        print(f"Topper: {name}")
        break

