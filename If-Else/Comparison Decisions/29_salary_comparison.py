# 29. Given two salaries, check who earns more.

salary1 = float(input("Enter the first salary: "))
salary2 = float(input("Enter the second salary: "))

if salary1 > salary2:
    print("The first person earns more.")
elif salary2 > salary1:
    print("The second person earns more.")
else:
    print("Both salaries are equal.")