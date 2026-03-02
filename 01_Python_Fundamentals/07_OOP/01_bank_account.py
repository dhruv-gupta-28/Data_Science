class BankAccount:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            print("Invalid balance")
        else:
            self._balance = value

# Test Code
if __name__ == "__main__":
    account = BankAccount()
    print(f"Initial balance: {account.balance}")
    
    print("Setting balance to 100...")
    account.balance = 100
    print(f"Current balance: {account.balance}")
    
    print("Trying to set negative balance (-50)...")
    account.balance = -50
    print(f"Final balance: {account.balance}")
