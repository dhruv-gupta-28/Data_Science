class Car:
    def set_details(self, brand, price):
        self.brand = brand
        self.price = price

    def print_details(self):
        print(f"Car Brand: {self.brand}, Price: {self.price}")

if __name__ == "__main__":
    c = Car()
    c.set_details("Toyota", 20000)
    c.print_details()
