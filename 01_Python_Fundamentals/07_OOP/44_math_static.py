class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"

if __name__ == "__main__":
    print(f"Add 5+3: {MathOperations.add(5, 3)}")
    print(f"Multiply 4*6: {MathOperations.multiply(4, 6)}")
    print(f"Divide 10/2: {MathOperations.divide(10, 2)}")
