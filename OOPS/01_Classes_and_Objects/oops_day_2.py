class Student:
    school="ABC High School"   # Class attribute shared by all instances    

    # instance method
    def hello(cls,a):
        cls.a=a
        print(cls.a,cls.school )

    # Class Method
    # def greet(cls,b):
    #     print(b)
    #     print(cls.school)

    

obj=Student()