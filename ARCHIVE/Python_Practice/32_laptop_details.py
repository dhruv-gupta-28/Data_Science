class Laptop:
    def set_specs(self, brand, ram):
        self.brand = brand
        self.ram = ram

    def display(self):
        print(f"Laptop: {self.brand}, RAM: {self.ram}GB")

if __name__ == "__main__":
    l = Laptop()
    l.set_specs("Dell", 16)
    l.display()
