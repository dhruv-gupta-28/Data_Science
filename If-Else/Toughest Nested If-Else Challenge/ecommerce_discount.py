# ❓ Problem Statement
# You are designing an e-commerce system that applies discounts based on customer type, cart value, and payment method.
# You must use nested if–else conditions (no loops, no ternary).

# 📌 Conditions
# 1️⃣ Premium Member
#    If cart value > $500 → 20% discount
#    Else if cart value 200–500 → 10% discount
#    Else → 5% discount
#
# 2️⃣ Regular Member
#    If cart value > $500
#       If payment method = Credit Card → 15% discount
#       Else → 10% discount
#    Else if cart value 200–500 → 7% discount
#    Else → 2% discount
#
# 3️⃣ Guest User
#    If cart value > $500 → 5% discount
#    Else → 0% discount

# 🔹 Example Inputs & Outputs
# ✔ Example 1
# Input:
# customerType = "Regular"
# cartValue = 600
# paymentMethod = "Credit Card"
# Output:
# Discount = 15%
#
# ✔ Example 2
# Input:
# customerType = "Premium"
# cartValue = 250
# paymentMethod = "Cash"
# Output:
# Discount = 10%

customer_type = input("Enter customer type (Premium/Regular/Guest): ")
cart_value = float(input("Enter cart value: $"))
payment_method = input("Enter payment method (Credit Card/Cash/etc.): ")

discount = 0

if customer_type == "Premium":
    if cart_value > 500:
        discount = 20
    elif cart_value >= 200:
        discount = 10
    else:
        discount = 5
elif customer_type == "Regular":
    if cart_value > 500:
        if payment_method == "Credit Card":
            discount = 15
        else:
            discount = 10
    elif cart_value >= 200:
        discount = 7
    else:
        discount = 2
elif customer_type == "Guest":
    if cart_value > 500:
        discount = 5
    else:
        discount = 0
else:
    print("Invalid customer type. Please enter Premium, Regular, or Guest.")
    discount = 0

print(f"Discount = {discount}%")
