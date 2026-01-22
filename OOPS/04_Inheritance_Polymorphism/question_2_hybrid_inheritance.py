class Base2:
    def get_value(self):
        return 20

class Level1(Base2):
    def get_value(self):
        return Base2.get_value(self) * 2

class Level2(Base2):
    def get_value(self):
        return Base2.get_value(self) - 5

class Final2(Level1, Level2):
    def get_value(self):
        val1 = Level1.get_value(self) # (20 * 2) = 40
        val2 = Level2.get_value(self) # (20 - 5) = 15
        return (val1 + val2) / 3

if __name__ == "__main__":
    print("--- Question 2 ---")
    q2 = Final2()
    print(f"Final Answer: {q2.get_value()}")
