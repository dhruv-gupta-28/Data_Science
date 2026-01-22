class Base3:
    def get_value(self):
        return 10

class Way1(Base3):
    def get_value(self):
        return Base3.get_value(self) + 5

class Way2(Base3):
    def get_value(self):
        return Base3.get_value(self) + 10

class Final3(Way1, Way2):
    def get_value(self):
        val1 = Way1.get_value(self) # (10 + 5) = 15
        val2 = Way2.get_value(self) # (10 + 10) = 20
        return val1 + val2

if __name__ == "__main__":
    print("--- Question 3 ---")
    q3 = Final3()
    print(f"Final Value: {q3.get_value()}")
