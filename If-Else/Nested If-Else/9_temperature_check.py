# 9. Given temperature, print "Cold" (<10), "Moderate" (10–30), "Hot" (>30).

temperature = float(input("Enter the temperature: "))

if temperature < 10:
    print("Cold")
else:
    if temperature <= 30:
        print("Moderate")
    else:
        print("Hot")