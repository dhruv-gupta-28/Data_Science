class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def gage(self):
        print(self.age)

m=Student("Harsh",20)
print(m.age)
m2=Student("Harshita",12)
m2.age=23               # Modifying age directly
print(m2.age)

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @property
    def get_age(self):
        print(f"My name is {self.name} and my age is {self.age}")

    @get_age.setter
    def set_age(self,age):
            if self.age>0:
                 self.age=age
            else:
                 print("Age Should not be negative")
obj=Student("Harsh",25)
obj.set_age=23
obj.get_age