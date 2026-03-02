class Employee:
    def set_salary(self, salary):
        self.salary = salary

    def increase_salary(self, amount):
        self.salary += amount
        print(f"Salary increased by {amount}")

    def display_salary(self):
        print(f"Updated Salary: {self.salary}")

if __name__ == "__main__":
    emp = Employee()
    emp.set_salary(40000)
    emp.increase_salary(5000)
    emp.display_salary()
