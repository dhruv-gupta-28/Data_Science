from abc import ABC, abstractmethod

class Appliance(ABC):
    @abstractmethod
    def power_consumption(self):
        pass

if __name__ == "__main__":
    print("Attempting to instantiate abstract class Appliance...")
    try:
        a = Appliance()
    except TypeError as e:
        print(f"Caught expected error: {e}")
