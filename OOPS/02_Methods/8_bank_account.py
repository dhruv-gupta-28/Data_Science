"""
8. Create a class `BankAccount` with:
   - instance variable `balance`
   - method `deposit(amount)`
   - method `withdraw(amount)`
"""

class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}. New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds!")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount}. New Balance: {self.balance}")

if __name__ == "__main__":
    acc = BankAccount()
    acc.deposit(1000)
    acc.withdraw(500)
    acc.withdraw(700)
