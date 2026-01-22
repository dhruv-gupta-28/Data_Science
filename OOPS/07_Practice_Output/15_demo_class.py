"""
15. Write a class `Demo` with:
    - class variable `x = 10`
    - instance method that changes `x` using class name
    - print value before and after method call
"""

class Demo:
    x = 10

    def change_x(self):
        print(f"Before change logic in method, Demo.x is: {Demo.x}")
        Demo.x = 20

if __name__ == "__main__":
    d = Demo()
    print(f"Initial x: {Demo.x}")
    d.change_x()
    print(f"Final x after method call: {Demo.x}")
