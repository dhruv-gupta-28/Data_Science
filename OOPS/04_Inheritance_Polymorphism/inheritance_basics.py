# Inheritance in Python

"""
When a class acquire instances and attributes of base class it is referred as Inheritance. 

Base Class ||       Parent Class
Derived Class ||    Child Class

Types : 
-Single Inheritance
-Multiple Inheritance
-Multi-Level Inheritance
-Hybrid Inheritance
-Hierarchial Inheritance 

"""

# # Single Inheritance
# class Parent:
#     def pdetails(self):
#         print("I am Parent")

# class Child(Parent):
#     def cdetails(self):
#         print("I am Child")

# obj=Child()
# obj.pdetails()

# # Multiple Inheritance 
# class Father:

#     def fdetails(self):
#         print("I am Father")

# class Mother:
#     def mdetails(self):
#         print("I am Mother")

# class Child(Father,Mother):
#     def cdetails(self):
#         print("I am Child")
# obj=Child()
# obj.fdetails()
# obj.mdetails()
# obj.cdetails()

# # Multi-Level Inheritance
# class Grandfather:
#     def gdetails(self):
#         print("I am Grandfather")
# class Father(Grandfather):
#     def fdetails(self):
#         print("I am Father")
# class Child(Father):
#     def cdetails(self):
#         print("I am Child")
# obj=Child()
# obj.gdetails()
# obj.fdetails()
# obj.cdetails()

# # Hierarchial Inheritance

# class Parent:
#     def pdetails(self):
#         print("I am Parent")

# class Child1(Parent):
#     def c1details(self):
#         print("I am Child 1")
# class Child2(Parent):
#     def c2details(self):
#         print("I am Child 2")

# obj1=Child1()
# obj1.pdetails()
# obj1.c1details()
# obj2=Child2()
# obj2.pdetails()

# # Hybrid Inheritance
# class Grandfather:
#     def gdetails(self):
#         print("I am Grandfather")
# class Father(Grandfather):
#     def fdetails(self):
#         print("I am Father")
# class Uncle(Grandfather):
#     def udetails(self):
#         print("I am Uncle")
# class Child(Father,Uncle):
#     def cdetails(self):
#         print("I am Child")


# Super Keyword
# class Parent:
#     def show(self):
#         print("I am Parent")
# class Child(Parent):
#     def show(self):
#         super().show()
#         print("I am Child")
# obj=Child()  
# obj.show()


class A:
    def show(self):
        print("A ka Show")

class B(A):
    def show(self):
        super().show()
        print("B ka Show")

class C(A):
    def show(self):
        super().show()
        print("C ka Show")
class D(B,C):
    pass

obj=D()
obj.show()
print(D.mro())

""" 
Diamond Problem in Inheritance  : 
is a problem caused when two classes B and C inherit from a common superclass A, and class D inherits from both B and C. 
This creates ambiguity in the inheritance hierarchy, as D has two paths to inherit from A (through B and C).


MRO : Method Resolution Order :
It is the order in which Python looks for a method in a hierarchy of classes.
Python uses theC3 Linearization Algorithm.

 
"""