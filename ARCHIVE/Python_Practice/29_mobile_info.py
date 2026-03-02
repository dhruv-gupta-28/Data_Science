class Mobile:
    def set_details(self, brand, price):
        self.brand = brand
        self.price = price

    def print_info(self):
        print(f"Mobile: {self.brand}, Price: {self.price}")

if __name__ == "__main__":
    m = Mobile()
    m.set_details("Apple", 80000)
    m.print_info()
