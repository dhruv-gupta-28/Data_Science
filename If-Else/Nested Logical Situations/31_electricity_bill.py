# 31. Electricity Bill: If units ≤100 → ₹5/unit, if 101–200 → ₹8/unit, if >200 → ₹10/unit.

units = float(input("Enter the number of units consumed: "))

if units <= 100:
    bill = units * 5
    print(f"Electricity bill: ₹{bill}")
elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 8)
    print(f"Electricity bill: ₹{bill}")
else:
    bill = (100 * 5) + (100 * 8) + ((units - 200) * 10)
    print(f"Electricity bill: ₹{bill}")