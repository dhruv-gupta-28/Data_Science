"""
9. Create a class `MathOperations` with static methods:
   - `add(a, b)`
   - `multiply(a, b)`
   - `divide(a, b)`
"""

class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b

if __name__ == "__main__":
    print(f"Add: {MathOperations.add(5, 3)}")
    print(f"Multiply: {MathOperations.multiply(4, 2)}")
    print(f"Divide: {MathOperations.divide(10, 2)}")
