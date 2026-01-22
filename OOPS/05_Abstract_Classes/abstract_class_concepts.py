# ABstract Class in Python
"""
Docstring for OOP's.Abstract Class

Abstract Class : is an Blueprint for other classes. It allows you to create a set of methods that must be created within any child classes built from the abstract class. A class which contains one or more abstract methods is called an abstract class. An abstract method is a method that is declared, but contains no implementation.

We don't create object of abstract Class Directly .
"""
from abc import ABC, abstractmethod

class Vehicle(ABC): 
    
    def infotainment_system(self):
        pass

    @abstractmethod
    def airbags(self):
        pass

class Car(Vehicle):

    def infotainment_system(self):
        print("Infotainment System: Touchscreen Display, Bluetooth Connectivity, Navigation System")

    def airbags(self):
        print("Car Airbags: Front and Side Airbags for Driver and Passenger")

obj=Car()
obj.infotainment_system()
obj.airbags()
