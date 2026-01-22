"""
13. Create an abstract class `Payment` with:
    - abstract method `pay()`
    - normal method `info()` that prints "Payment Process"
"""
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

    def info(self):
        print("Payment Process")

class CreditCardPayment(Payment):
    def pay(self):
        print("Paid via Credit Card")

if __name__ == "__main__":
    p = CreditCardPayment()
    p.info()
    p.pay()
