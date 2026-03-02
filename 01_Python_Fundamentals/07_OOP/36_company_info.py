
class Company:
    def set_info(self, name, location):
        self.name = name
        self.location = location

    def display(self):
        print(f"Company: {self.name}, Location: {self.location}")

if __name__ == "__main__":
    c = Company()
    c.set_info("Google", "Mountain View")
    c.display()
