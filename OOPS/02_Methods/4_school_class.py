"""
4. Create a class `School` with:
   - class variable `pass_marks = 33`
   - class method `update_pass_marks(marks)`
   - print updated pass marks
"""

class School:
    pass_marks = 33

    @classmethod
    def update_pass_marks(cls, marks):
        cls.pass_marks = marks

if __name__ == "__main__":
    print(f"Original Pass Marks: {School.pass_marks}")
    School.update_pass_marks(40)
    print(f"Updated Pass Marks: {School.pass_marks}")
