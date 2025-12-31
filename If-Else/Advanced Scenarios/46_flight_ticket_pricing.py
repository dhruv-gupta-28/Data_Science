# 46. Flight ticket pricing by age (<12 half, 12–60 full, >60 30% discount).

base_price = float(input("Enter the base ticket price: ₹"))
age = int(input("Enter the passenger's age: "))

if age < 12:
    ticket_price = base_price * 0.5  # Half price
    print(f"Ticket price (50% discount for children): ₹{ticket_price}")
elif age <= 60:
    ticket_price = base_price  # Full price
    print(f"Ticket price (full price): ₹{ticket_price}")
else:
    ticket_price = base_price * 0.7  # 30% discount
    print(f"Ticket price (30% discount for seniors): ₹{ticket_price}")

