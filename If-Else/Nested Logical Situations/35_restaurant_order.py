# 35. Restaurant Order: If food type = “Veg”, suggest Paneer; if “Non-Veg”, suggest Chicken; else suggest Salad.

food_type = input("Enter your food preference (Veg/Non-Veg): ").lower()

if food_type == "veg":
    print("We suggest Paneer.")
elif food_type == "non-veg":
    print("We suggest Chicken.")
else:
    print("We suggest Salad.")