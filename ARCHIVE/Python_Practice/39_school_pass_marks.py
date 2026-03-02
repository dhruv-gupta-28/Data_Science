class School:
    pass_marks = 33

    @classmethod
    def update_pass_marks(cls, marks):
        cls.pass_marks = marks
        print(f"Updated pass marks to: {cls.pass_marks}")

if __name__ == "__main__":
    print(f"Original Pass Marks: {School.pass_marks}")
    School.update_pass_marks(40)
