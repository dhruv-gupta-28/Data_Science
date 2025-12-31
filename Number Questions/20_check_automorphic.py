# 20. Check if a number is Automorphic
# Last digits of its square are same as the number
# Example: 25² = 625 → ends with 25

num = int(input("Enter a number: "))
square = num ** 2
num_str = str(num)
square_str = str(square)

if square_str.endswith(num_str):
    print(f"{num} is an Automorphic number.")
    print(f"Proof: {num}² = {square} (ends with {num})")
else:
    print(f"{num} is not an Automorphic number.")
    print(f"Proof: {num}² = {square} (does not end with {num})")

