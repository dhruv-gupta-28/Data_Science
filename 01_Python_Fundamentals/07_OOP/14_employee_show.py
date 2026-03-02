class Employee:
    def __init__(self, name):
        self.name = name
    
    def show(self):
        print(self.name)

if __name__ == "__main__":
    emp = Employee("John Doe")
    emp.show()
