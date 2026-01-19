"""
Docstring for Errorhandling

Exception Handling :
It is a practice to handle exceptions that may occur during the execution of a program.
Exception handling does not prevent syntax errors but deals with exceptions that occur during program execution.


Types of Error :
-Syntax Error : When we have written something wrong in the syntax of the programming language.
-Logical Error : When we get undesired output due to a mistake in the logic of the program.
-Runtime Error : When an error occurs during the execution of the program.

Keywords used in Exception Handling :
-Try : The code that may cause an exception is placed inside the try block.
-Except : The code that handles the exception is placed inside the except block.
-finally : The code inside the finally block will always execute, regardless of whether an exception occurred or not.


Common Errors in Python :
-ZeroDivisionError : When a number is divided by zero.
-IndexError : When trying to access an index that is out of range in a list or string.
-KeyError : When trying to access a key that does not exist in a dictionary.
-FileNotFoundError : When trying to access a file that does not exist.
-TypeError : When an operation is performed on incompatible data types.
-ValueError : When a function receives an argument of the correct type but an inappropriate value.
li.index()
"""
# print(1/0)

try:
    print("Hello World")
    print("You are inside try block")
    print("a"+5)
    print("End of try block")
except ValueError as ve:
    print("Value Error occurred", ve)
except Exception as e :
    print("Error occurred", e)
finally:
    print("This will execute no matter what")

# Assert Keyword
"""
The assert keyword is used to test if a condition is true.
If the condition is false, an AssertionError is raised.
"""
x=10
y=5
try : 
    assert x<y, "x is not less than y"
except AssertionError as ae:
    print("Assertion Error:", ae)

# Raise Keyword
"""
raise Keyword is used to raise an exception manually.
For example, if a certain condition is not met, we can raise an exception to indicate an error.
"""
age=int(input("Enter your age: "))
if age<18:
    raise ValueError("You are not eligible to vote")
else:
    print("You Can vote")