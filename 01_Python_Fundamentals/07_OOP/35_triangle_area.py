class Triangle:
    def set_dimensions(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        area = 0.5 * self.base * self.height
        print(f"Area of Triangle: {area}")

if __name__ == "__main__":
    t = Triangle()
    t.set_dimensions(10, 8)
    t.calculate_area()
