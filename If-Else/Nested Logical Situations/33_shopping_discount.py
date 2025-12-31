# 33. Shopping Discount: If bill > ₹5000 → 20% discount, if 2000–5000 → 10% discount, else no discount.

bill = float(input("Enter your total bill amount: "))

if bill > 5000:
    discount = 0.2  # 20% discount
    final_bill = bill * (1 - discount)
    print(f"Final bill with 20% discount: ₹{final_bill}")
elif bill >= 2000:
    discount = 0.1  # 10% discount
    final_bill = bill * (1 - discount)
    print(f"Final bill with 10% discount: ₹{final_bill}")
else:
    print(f"Final bill: ₹{bill}")