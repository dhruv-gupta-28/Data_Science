class Person:
    def set_info(self, name, city):
        self.name = name
        self.city = city
    
    def display_info(self):
        print(f"Name: {self.name}, City: {self.city}")

if __name__ == "__main__":
    p = Person()
    p.set_info("Alice", "New York")
    p.display_info()
