"""
From & import : 
From is a keyword which defines from where we want a module or function
import is a keyword which defines which function file or module we need .

*(asterisk) : This is used to import all the functions from a module or file .
"""
from Function2 import *
def calc():
    n1=int(input("Enter Number : "))
    n2=int(input("Enter Number : "))
    ch=input("Enter +,-,*,/ : ")
    if ch=="+":
        print(add(n1,n2))
    elif ch=="-":
        print(subtract(n1,n2))
    elif ch=="*":
        print(multiply(n1,n2))
    elif ch=="/":
        print(divide(n1,n2))
    else:
        print("Enter Valid Operator")