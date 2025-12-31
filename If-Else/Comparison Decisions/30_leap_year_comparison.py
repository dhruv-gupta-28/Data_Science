# 30. Compare two years and decide which is a leap year.

year1 = int(input("Enter the first year: "))
year2 = int(input("Enter the second year: "))

# Check if year1 is leap year
if year1 % 400 == 0:
    year1_leap = True
elif year1 % 100 == 0:
    year1_leap = False
elif year1 % 4 == 0:
    year1_leap = True
else:
    year1_leap = False

# Check if year2 is leap year
if year2 % 400 == 0:
    year2_leap = True
elif year2 % 100 == 0:
    year2_leap = False
elif year2 % 4 == 0:
    year2_leap = True
else:
    year2_leap = False

if year1_leap and not year2_leap:
    print(f"{year1} is a leap year.")
elif year2_leap and not year1_leap:
    print(f"{year2} is a leap year.")
elif year1_leap and year2_leap:
    print("Both years are leap years.")
else:
    print("Neither year is a leap year.")