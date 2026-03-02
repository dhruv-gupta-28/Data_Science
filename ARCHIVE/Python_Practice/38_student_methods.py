class Student:
    def __init__(self):
        self.name = ""
        self.marks = 0

    def set_details(self, name, marks):
        self.name = name
        self.marks = marks

    def get_details(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

if __name__ == "__main__":
    # Question 3 asks for two objects
    s1 = Student()
    s1.set_details("Rahul", 85)
    
    s2 = Student()
    s2.set_details("Sonia", 92)

    print("Student 1:")
    s1.get_details()
    
    print("Student 2:")
    s2.get_details()
