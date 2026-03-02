class BankAccount:
    def set_balance(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")

    def display_balance(self):
        print(f"Current Balance: {self.balance}")

if __name__ == "__main__":
    acc = BankAccount()
    acc.set_balance(1000)
    acc.deposit(500)
    acc.display_balance()
