class Rectangle:
    def __init__(self):
        self._length = 0
        self._breadth = 0

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if value >= 0:
            self._length = value
        else:
            print("Length cannot be negative")

    @property
    def breadth(self):
        return self._breadth

    @breadth.setter
    def breadth(self, value):
        if value >= 0:
            self._breadth = value
        else:
            print("Breadth cannot be negative")

    @property
    def area(self):
        return self._length * self._breadth

# Test Code
if __name__ == "__main__":
    rect = Rectangle()
    
    print("Setting length=10, breadth=5...")
    rect.length = 10
    rect.breadth = 5
    print(f"Area: {rect.area}")
    
    print("Changing length to 20...")
    rect.length = 20
    print(f"Updated Area: {rect.area}")
