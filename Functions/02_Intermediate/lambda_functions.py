def add(a, b):
    return a + b

obj = lambda x , y : x + y
print(obj(2,3))

# Map || Reduce || Filter 

li=[1,2,3,4,5]
def square(n):
    return n*n
li1=list(map(square,li))
print(li1)

li2=list(map(lambda n:n*n,li))
print(li2)

# Filter
def is_even(n):
    return n%2==0
li3=list(filter(is_even,li))
print(li3)  # [2,4]

# Reduce 
from functools import reduce
def add(x,y):
    return x+y
result=reduce(add,li)
print(result)  # 15


# Command  to create virtual environment
# python -m venv myenv
# Command to activate virtual environment
# myenv\Scripts\activate (Windows)
# source myenv/bin/activate (Mac/Linux)

# command to deactivate virtual environment
# deactivate