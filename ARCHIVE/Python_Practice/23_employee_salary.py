class Employee:
    def set_data(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

if __name__ == "__main__":
    emp = Employee()
    emp.set_data("John", 50000)
    emp.display()
