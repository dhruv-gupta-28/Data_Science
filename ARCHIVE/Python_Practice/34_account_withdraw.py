class Account:
    def set_balance(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient funds")

    def display_balance(self):
        print(f"Remaining Balance: {self.balance}")

if __name__ == "__main__":
    acc = Account()
    acc.set_balance(5000)
    acc.withdraw(1000)
    acc.display_balance()
