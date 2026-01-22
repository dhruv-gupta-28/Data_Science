# Access Modifiers in Python
"""
    In Python, access modifiers are used to set the accessibility of class members (attributes and methods).
    There are three types of access modifiers:
    
    1. Public: Members declared as public are accessible from anywhere, both inside and outside the class.
       By default, all members in Python are public.
       
    2. Protected: Members declared as protected are accessible within the class and its subclasses.
       In Python, a member is considered protected if its name starts with a single underscore (_).
       
    3. Private: Members declared as private are accessible only within the class itself.
       In Python, a member is considered private if its name starts with a double underscore (__).
"""
# class Student:
#     def public_method(self,Name,Age):
#         self.Name=Name      #Public Attribute
#         self.Age=Age
#         print("This is a public method.")

# obj=Student()
# obj.public_method("Harsh",20)
# print("Name:",obj.Name)

# class Student:
#     def protected_method(self,Name,Age):
#         self._Name=Name      #Protected Attribute
#         self._Age=Age
#         print("This is a protected method.")
# obj=Student()
# obj.protected_method("Harshita",22)
# print("Name:",obj._Name)
# print("Age:",obj._Age)

class Student:
    def private_method(self,Name,Age):
        self.__Name=Name      #Private Attribute
        self.__Age=Age
        print("This is a private method.")
obj=Student()
obj.private_method("Harman",23)
#print("Name:",obj.__Name)   # This will raise an AttributeError
#print("Age:",obj.__Age)     # This will raise an AttributeError
# Accessing private attributes using name mangling
print("Name:",obj._Student__Name)
print("Age:",obj._Student__Age)

obj.private_method("Harsimran",24)
print("Name:",obj._Student__Name)
print("Age:",obj._Student__Age)