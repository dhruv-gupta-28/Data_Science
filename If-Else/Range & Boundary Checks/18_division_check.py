# 18. Check if a percentage lies in First Division (>60), Second Division (33–60), or Fail (<33).

percentage = float(input("Enter your percentage: "))

if percentage > 60:
    print("First Division")
elif percentage >= 33:
    print("Second Division")
else:
    print("Fail")