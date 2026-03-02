class Rectangle:
    def set_dimensions(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        area = self.length * self.breadth
        print(f"Area of Rectangle: {area}")

if __name__ == "__main__":
    r = Rectangle()
    r.set_dimensions(10, 5)
    r.calculate_area()
