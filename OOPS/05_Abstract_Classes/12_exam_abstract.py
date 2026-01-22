"""
12. Create an abstract class `Exam` with:
    - abstract method `result()`
    Do NOT implement the method and try to create an object (of a subclass without implementation).
"""
from abc import ABC, abstractmethod

class Exam(ABC):
    @abstractmethod
    def result(self):
        pass

class MidTerm(Exam):
    pass # Not implementing result()

if __name__ == "__main__":
    print("Attempting to instantiate subclass MidTerm without implementing abstract method...")
    try:
        e = MidTerm()
    except TypeError as e:
        print(f"Caught expected error: {e}")
