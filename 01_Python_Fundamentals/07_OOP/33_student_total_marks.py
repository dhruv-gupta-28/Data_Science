class Student:
    def set_marks(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def print_total(self):
        total = self.m1 + self.m2 + self.m3
        print(f"Total Marks: {total}")

if __name__ == "__main__":
    s = Student()
    s.set_marks(80, 90, 85)
    s.print_total()
