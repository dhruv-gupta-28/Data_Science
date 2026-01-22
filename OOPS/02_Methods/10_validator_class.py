"""
10. Create a class `Validator` with static method:
    - `is_positive(num)` -> returns True or False
"""

class Validator:
    @staticmethod
    def is_positive(num):
        return num > 0

if __name__ == "__main__":
    print(f"Is 10 positive? {Validator.is_positive(10)}")
    print(f"Is -5 positive? {Validator.is_positive(-5)}")
