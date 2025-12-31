# 27. Compare two weights and check if both are equal, or which one is heavier.

weight1 = float(input("Enter the first weight: "))
weight2 = float(input("Enter the second weight: "))

if weight1 == weight2:
    print("Both weights are equal.")
elif weight1 > weight2:
    print(f"The first weight ({weight1}) is heavier.")
else:
    print(f"The second weight ({weight2}) is heavier.")