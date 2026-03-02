class Mobile:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

if __name__ == "__main__":
    m = Mobile("Samsung", "Galaxy S24")
    print(f"Mobile Brand: {m.brand}, Model: {m.model}")
