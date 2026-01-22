"""
11. Create an abstract class `Appliance` with:
    - abstract method `power_consumption()`
    Try to create an object of this class and observe the error.
"""
from abc import ABC, abstractmethod

class Appliance(ABC):
    @abstractmethod
    def power_consumption(self):
        pass

if __name__ == "__main__":
    print("Attempting to instantiate abstract class Appliance...")
    try:
        obj = Appliance()
    except TypeError as e:
        print(f"Caught expected error: {e}")
