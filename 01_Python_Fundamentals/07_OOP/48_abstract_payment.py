from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

    def info(self):
        print("Payment Process")

class CreditCard(Payment):
    def pay(self):
        print("Paying via Credit Card")

if __name__ == "__main__":
    cc = CreditCard()
    cc.info()
    cc.pay()
