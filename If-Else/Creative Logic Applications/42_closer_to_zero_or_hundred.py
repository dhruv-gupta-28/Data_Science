# 42. Check if a number is closer to 0 or 100.

num = float(input("Enter a number: "))

distance_to_zero = abs(num - 0)
distance_to_hundred = abs(num - 100)

if distance_to_zero < distance_to_hundred:
    print("The number is closer to 0.")
elif distance_to_hundred < distance_to_zero:
    print("The number is closer to 100.")
else:
    print("The number is equidistant from 0 and 100.")

