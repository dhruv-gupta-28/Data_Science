    # Constructor's : 
"""
    Constructor's are the special function which have self calling feature as an object created .
"""

    # class Greet:

    #     def __init__(self):
    #         print("I am Everywhere...!")

    #     def morning(self):
    #         print("Good Morning")

    #     def noon(self):
    #         print("Good Afternoon")

    #     def night(self):
    #         print("Good Night")

    # obj=Greet()
    # obj.morning()
    # obj.night()

    # obj2=Greet()
    # obj2.night()

    # Application : 

class Shapes:

        def __init__(self,l,b):
            self.l=l 
            self.b=b

        def sq(self):
            return self.l*self.l
        
        def rect(self):
            return self.l*self.b 
        
        def cuboid(self,h):
            self.h=h
            return self.l*self.b 

        def circle(self,r):
            self.r=r
            return 3.14*self.r*self.r
obj=Shapes(5,10)
print("Square Area =",obj.sq())
print("Rectangle Area =",obj.rect())
print("Cuboid Area =",obj.cuboid(7))
print("Circle Area =",obj.circle(4))