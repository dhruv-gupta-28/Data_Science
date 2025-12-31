# 13. ATM withdrawal: If balance ≥ withdrawal, allow transaction, else show "Insufficient Balance".

balance = float(input("Enter your account balance: "))
withdrawal = float(input("Enter withdrawal amount: "))

if balance >= withdrawal:
    print("Transaction allowed.")
    print(f"Remaining balance: ₹{balance - withdrawal}")
else:
    print("Insufficient Balance")