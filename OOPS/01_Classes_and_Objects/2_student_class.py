"""
2. Create a class `Student` with:
   - instance variables `name` and `marks`
   - method `set_details()`
   - method `get_details()`
"""

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
    s1 = Student()
    s1.set_details("Rahul", 85)
    s1.get_details()
