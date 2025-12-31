# 11. A cinema ticket costs ₹100. If age <12 → 50% discount, if age >60 → 30% discount, else full price.

age = int(input("Enter your age: "))
base_price = 100

if age < 12:
    discount = 0.5  # 50% discount
    price = base_price * (1 - discount)
    print(f"Ticket price with 50% discount: ₹{price}")
elif age > 60:
    discount = 0.3  # 30% discount
    price = base_price * (1 - discount)
    print(f"Ticket price with 30% discount: ₹{price}")
else:
    print(f"Ticket price: ₹{base_price}")