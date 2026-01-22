# Recursion : 
"""

Recursion is a programming technique where a function calls itself in order to solve a problem. It typically involves a base case to terminate the recursion and a recursive case that breaks the problem down into smaller subproblems.
"""

# Factorial using recursion : 
def factorial(n):
    if n==1 or n==0:
        return 1
    else : 
        return n*factorial(n-1)

print(factorial(5))

"""
Using Loop : 

for i in range(1,n):
    prod=prod*i
    
"""

"""
Cases in Recursion :
1. Base Case : The condition under which the recursion stops. It prevents infinite recursion and eventual stack overflow.
2. Recursive Case : The part of the function where it calls itself with a modified argument, moving towards the base case.

Types of Recursion :
1. Direct Recursion : A function calls itself directly.
2. Indirect Recursion : A function calls another function, which in turn calls the first function.
"""
# Example of Indirect  Recursion
def even(n):
    if n==0:
        return True
    else:
        return odd(n-1)
def odd(n):
    if n==0:
        return False
    else:
        return even(n-1)
    

print(even(4))  # True
print(odd(7))   # True

"""
LOI :
Line of Indirection : 
The number of function calls that occur before reaching the base case in a recursive function.
"""

"""
LEGB Rule :
LEGB stands for Local, Enclosing, Global, and Built-in. It is the order
in which Python looks for variable names when they are referenced in the code.
1. Local (L): The innermost scope, which is the local scope of the current function.
2. Enclosing (E): The scope of any enclosing functions, which is the local scope
    of any and all enclosing functions.
3. Global (G): The global scope, which is the module-level scope.
4. Built-in (B): The outermost scope, which is the built-in names provided by Python.

"""