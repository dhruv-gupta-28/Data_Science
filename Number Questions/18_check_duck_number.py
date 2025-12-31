# 18. Check if a number is a Duck number
# A number with zero in it (but not at the start), e.g., 507 → Duck number

num = input("Enter a number: ")

if num[0] == '0':
    print(f"{num} is not a Duck number (starts with zero).")
elif '0' in num:
    print(f"{num} is a Duck number.")
else:
    print(f"{num} is not a Duck number (no zero present).")

