"""
3. Create **two objects** of the `Student` class with different data and print their details.
   (Reusing logic from Q2 directly or redefining simple class for standalone execution)
"""

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_details(self):
        print(f"Student: {self.name}, Scored: {self.marks}")

if __name__ == "__main__":
    s1 = Student("Amit", 90)
    s2 = Student("Priya", 95)

    print("--- Object 1 ---")
    s1.get_details()
    
    print("--- Object 2 ---")
    s2.get_details()
