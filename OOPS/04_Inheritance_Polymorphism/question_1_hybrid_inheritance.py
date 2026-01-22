class Base1:
    def get_value(self):
        return 10

class Path1(Base1):
    def get_value(self):
        # Explicitly calling Base1 to adhere to "separate path" logic
        # avoiding MRO chaining to Path2
        return Base1.get_value(self) + 5

class Path2(Base1):
    def get_value(self):
        return Base1.get_value(self) + 15

class Final1(Path1, Path2):
    def get_value(self):
        val1 = Path1.get_value(self) # (10 + 5) = 15
        val2 = Path2.get_value(self) # (10 + 15) = 25
        return val1 + val2 + 10

if __name__ == "__main__":
    print("--- Question 1 ---")
    q1 = Final1()
    print(f"Final Value: {q1.get_value()}")
