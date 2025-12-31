# 26. Compare two distances and print which one is farther.

distance1 = float(input("Enter the first distance: "))
distance2 = float(input("Enter the second distance: "))

if distance1 > distance2:
    print(f"The first distance ({distance1}) is farther.")
elif distance2 > distance1:
    print(f"The second distance ({distance2}) is farther.")
else:
    print("Both distances are equal.")