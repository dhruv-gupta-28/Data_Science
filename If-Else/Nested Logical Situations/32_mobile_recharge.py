# 32. Mobile Recharge: If plan = “Daily”, cost = ₹199; if “Weekly”, cost = ₹499; else ₹999.

plan = input("Enter your recharge plan (Daily/Weekly/Monthly): ").lower()

if plan == "daily":
    print("Cost: ₹199")
elif plan == "weekly":
    print("Cost: ₹499")
else:
    print("Cost: ₹999")