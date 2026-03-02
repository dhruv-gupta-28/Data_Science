class Circle:
    def set_radius(self, radius):
        self.radius = radius

    def calculate_area(self):
        area = 3.14 * self.radius * self.radius
        print(f"Area of Circle: {area}")

if __name__ == "__main__":
    c = Circle()
    c.set_radius(7)
    c.calculate_area()
