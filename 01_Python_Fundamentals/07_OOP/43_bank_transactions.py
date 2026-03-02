class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}, Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}, Balance: {self.balance}")
        else:
            print("Insufficient funds")

if __name__ == "__main__":
    acc = BankAccount()
    acc.deposit(1000)
    acc.withdraw(500)
    acc.withdraw(600)
