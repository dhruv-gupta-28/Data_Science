# Decorator's in Python : 
"""
Decorator is a special function which is used to wrap a function into another function.
"""
# args and kwargs:


def greet(fx):
    def mfx(n1,n2):
        print("Hello USer")
        fx(n1,n2)
        print("Thankyou For Using My Program")
    return mfx


"""
*args : It is used to pass multiple  arguments to a function.
**kwargs : It is used to pass multiple key value arguments to a function.

"""

def hello(fx):
    def mfx(*args,**kwargs):
        print("Hello USer")
        fx(*args,**kwargs)
        print("Thankyou For Using My Program")
    return mfx

@greet
def add(n1,n2):
    print("Sum =",n1+n2)

@hello
def subtract(n1,n2,n3):
    print("Sub =",n1-n2-n3)

add(5,7)
# @greet
# def add():
#     n1=int(input("Enter first number: "))
#     n2=int(input("Enter second number: "))
#     print("Sum =",n1+n2)

# add()

# @greet
# def subtract():
#     n1=int(input("Enter first number: "))
#     n2=int(input("Enter second number: "))
#     print("Sub =",n1-n2)
    

