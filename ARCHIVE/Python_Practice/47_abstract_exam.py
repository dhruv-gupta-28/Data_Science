from abc import ABC, abstractmethod

class Exam(ABC):
    @abstractmethod
    def result(self):
        pass

class MidTerm(Exam):
    # Intentionally NOT implementing result to show error
    pass

if __name__ == "__main__":
    print("Attempting to instantiate subclass MidTerm without implementing abstract method...")
    try:
        e = MidTerm()
    except TypeError as e:
        print(f"Caught expected error: {e}")
