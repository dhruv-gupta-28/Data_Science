from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def airbags(self):
        print("It is Mandatory")
        
    def infotainment(self):
        print("It is Optional")
        
class Tata(Vehicle):
    def airbags(self):
        print("Tata Airbags deployed")
    
    def safety(self):
        print("I am Tata")
        
if __name__ == "__main__":
    obj = Tata()
    obj.safety()
    obj.airbags()
    obj.infotainment()
