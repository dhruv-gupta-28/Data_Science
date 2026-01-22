"""
POP : Stands for Procedural Oriented Programming it is a programming paradigm which uses procedure calls to operate on data. It follows top down approach and focuses on functions or procedures to operate on data.

OOP's Stands for Object Oriented Programming it is a paradigm which uses real world entities in Programming. It uses principle of DRY (Don't Repeat Yourself) and makes code reusable.

Pillars of OOP's:
1.Classes
2.Objects
3.Inheritance
4.Polymorphism
5.Abstraction
6.Encapsulation
"""

"""
Classes : A class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.
Objects : An object is an instance of a class. It is created using the class blueprint and can have its own unique attributes and behaviors.
"""

class Employee:
    # Attributes  :  
    company = "Google"
    name="John"
    salary=100000
    role="Developer"

obj=Employee()
print(obj.company)
print(obj.name)
print(obj.salary)
print(obj.role)

obj2=Employee()
print(obj2.company)
obj2.name="Doe"  # Changing the name attribute for obj2
print(obj2.name)
