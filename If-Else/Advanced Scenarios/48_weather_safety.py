# 48. Weather safety: <0 = Freezing, 0–40 = Safe, >40 = Danger.

temperature = float(input("Enter the temperature: "))

if temperature < 0:
    print("Freezing")
elif temperature <= 40:
    print("Safe")
else:
    print("Danger")

