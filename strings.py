"""
Strings are the collection of characters used to store and manipulate text data in programming.

Strings are IMmutable .
"""
# Declaration of Strings : 
a="Harsh"
print(a)
print(type(a))

# String Indexing and Length : 
# Length : Total Number of Characters
# Index : Position of Characters (Starting from 0)
a="Amrtisar"
print(len(a))
print(a[0])  # First Character
# variablename[index_Number]
print(a[4])
# print(a[8])

# String Concatination :
"""
Joining Two or More Strings Together is reffered as String Concatination.
"""
a="Hello"
b="World"
print(a+" "+b)

# Escape Sequences : 
"""
Definition : 
These are the special characters which get ignored by the message box and perform ther functionality .
"""
print("Hello @")
print("I am a Developer")
print("I am a \"Developer\"")
print("i am a \nDeveloper ")
print("I am a :\tDeveloper")

# String Formatting : 
"""
It is used to display variables in between of the messages majorly .
"""
a="Car"
b=1000
print("The Price of Car is 1000 .")
print("The Price of",a,"is",b,".")
print(f"The Price of {a} is {b} .")
print(f"The Price of {a} is {b} . ".format(a,b))

# String Methods : 
a="harsh"
print(a.upper())
print(a.lower())
print(a.capitalize())
print(a.replace('h','j'))
print(a.count('h'))

# String Slicing : 
"""
It is a way which is used to extract a portion of string by specifying the start and end index .
syntax : variablename[startindex:endindex:step]
by default step=1
by default startindex=0
by default endindex=length of string
"""
a="Amritsar"
print(a)
print(a[0])
print(a[0:5:1])
print(a[0:5:2])

b="Tiruvanthpuram"
print(b[0:9:5])
print(b[::2])

# Negative Indexing and Slicing :
"""
Negative Indexing : It is used to access the characters from the end of the string .
Negative Slicing : It is used to extract a portion of string from the end of the string .
"""
a="AMRITSAR"
b="Tiruvanthpuram"
# marupht
print(a[-1])
print(a[-4])
print(b[-1:-8:-1])
print(b[-8:-1:1])

# If Else Statements : 
"""
statements : 
    block of code which gets executed once .
loops :
    block of code which gets executed till the conditions remains true .

If-else Statement : 
These statements deals with conditional operators .
4 types : 
    -Only If
    -If Else
    -if elif else || If-else Ladder
    -Nested If-else

syntax : 
if (condition):
    statements


Indentation : is the space provided from borderline . 
"""

# Only If : 
age=int(input("Enter Age : "))
if age>=18:
    print("You Can Vote...")
print("Thankyou")

# IF-Else : 
age=int(input("Enter Age  : "))
if age>=18:
    print("You can vote")
else : 
    print("You Can Not Vote")
print("Thankyou")

# If-Else Ladder :
num=int(input("Enter Number : "))
if num>0:
    print("Number is Positive")
elif num <0 :
    print("Number is Negative")
else:
    print("Number is Neutral")

# Nested If-Else : 
num=int(input("Enter Number : "))
if num>0:
    if num==7:
        print("Congrats, Its a Lucky Number")
    print("Thankyou")
else :
    print("Please Enter Positive Number ")