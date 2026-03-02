class Product:
    def __init__(self):
        self._price = 0

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            print("Price cannot be negative")

    @property
    def discounted_price(self):
        return self._price * 0.9 # 10% discount means 90% of price

# Test Code
if __name__ == "__main__":
    p = Product()
    
    print("Setting price to 100...")
    p.price = 100
    
    print(f"Price: {p.price}")
    print(f"Discounted Price (10% off): {p.discounted_price}")
