"""
Docstring for .Polymorphism

Polymorphism is a core concept in Object-Oriented Programming (OOP) that allows methods to do different things based on the object it is acting upon, even though they share the same name. This can be achieved through method overriding and method overloading.
 
Poly="many", morphism="forms"

-Functional Polymorphism
-Operator Polymorphism
-Method Overriding
-Method Overloading Soln(Using Default Argument,Using *args)
"""

# Functional Polymorphism
a="Hello"
b=[1,2,3,4]
print(len(a))
print(len(b))

# Operator Polymorphism
print(5+10)          # Integer Addition
print("Hello"+" World")  # String Concatenation

# Method Overriding
class Animal:
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
obj=Dog()
obj.sound()

# Duck Typing : 
"""
Duck Typing is a concept related to polymorphism in Python where the type or class of an object is less important than the methods it defines.

Python Says : 
"If it looks like a duck and quacks like a duck, it's a duck."
"""

class Cat:
    def speak(self):
        print("Meow")
class Cow:
    def speak(self):
        print("Moo")
def animal_sound(animal):
    animal.speak()
cat=Cat()
cow=Cow()
animal_sound(cat)
animal_sound(cow)

"""
Python Uses EAFP Principle :
Easier to Ask Forgiveness than Permission

LBYL :
Look Before You Leap
"""
# EAFP Example
def make_sound(animal):
    try:
        animal.speak()
    except AttributeError:
        print("This animal cannot speak")
class Dog:
    def speak(self):
        print("Woof")
dog=Dog()
make_sound(dog)  # Works fine

# LBYL Example
def make_sound_lbyl(animal):
    if hasattr(animal, 'speak'):
        animal.speak()
    else:
        print("This animal cannot speak")
