# Functions : 
"""
    Block of code which gets executed when they are invoked are reffered as Functions.
    Pre-Defined Function : 
        Functions which are already declared in main class .
        print,input,type etc

    User-Defined Function : 
    Functions created by user according to their requirement .

    these are declared using def keyword .

    syntax : 
    def functionname(parameters):
        statement 


    parameter(s) : Passed While declaring a function
    argument : declared while calling a function
    return : This return the value asked for .

    Types of User Defined Function : 
    -NANR : No Argument No return
    -NAWR : No Argument With Return
    -WANR : With Argument No Return
    -WAWR : With Argument With Return    
"""

# # Function Declaration
# def greet(n):
#     return n


# # Calling a Function || Invoking a Function
# greet("Harsh")
# print(greet("Harsh"))
# x=greet("Harish")
# print(x)

# # NANR : 
# def greet():
#     print("Hello")

# # NAWR : 
# def greet():
#     return "HARSH"

# # WANR : 
# def greet(n):
#     print(n)
# greet("Harshita")

# # WAWR : 
# def greet(m):
#     return m
# print(greet("Harish"))

# Modules || Packages  || Library :
# Modules : A file consisting of python code (functions,variables etc) is called module . 
# Packages : A collection of modules is called package .
# Library : A collection of packages is called library .

"""
datetime , random , math , os 

Pip : Python Installer Package is used to install external packages .
pip freeze : Lists all the installed packages in the current environment

pip install packagename : used to install a package
pip uninstall packagename : used to uninstall a package
"""

# Importing a module
import math
from math import sqrt , factorial
print(math.sqrt(16))
print(math.__dict__)
print(math.factorial(5))
print(math.ceil(4.1))
print(math.floor(4.7))
print(math.gcd(12,15))
print(math.isclose(0.1+0.1,0.3))

import datetime
print(datetime.date.today())
print(datetime.datetime.now())
now1=datetime.datetime.now()
print(now1.year)
x=now1.month
print(x)
print(type(x))
print(now1.day)
print(now1.hour)
print(now1.minute)
print(now1.second)
print(now1.strftime("%H:%M:%S"))
print(now1.strftime("%d/%m/%Y"))
print(now1.strftime("%A"))
print(now1.strftime("%a"))

import random
print(random.randint(100000,999999))
print(random.random())