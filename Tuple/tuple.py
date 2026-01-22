# Tuple : 
"""
Tuple is a non-primitive data type which can hold multiple values .
Tuple is heterogenous nature  .
tuple is declared by "()".

Properties : 
-Immutable
-Ordered
-Allows Duplicacy
"""
tup=(1,2,3,4,5,6)
li=[1,2,3,4,5,6]

li[0]="A"
print(li)
print(tup)
print(type(tup))

# Ordered 
print(li[0])
print(tup[0])

# Indexing and Length : 
print(len(tup))
print(tup[0])
print(tup[-1])          #Negative Indexing

tup=(1,2,3,4,5)
tup[4]
print(tup[-5])

# Tuple Slicing : 
"""
print(tup[start(inclusive):end(exclusive):step])
"""
print(tup[::2])

# Tuple Creation : 
tup1=(1,2,3,4,5)
tup2=(1,2.3,"A",True)
tup3=(1,)       #Single Element tuple
tup4=((1,2),(3,4)) #Nested Tuple 

# Tuple operation : 
"""Concatination"""
tup1=(1,2,3)
tup2=(4,5,6)
print(tup1+tup2)
"""Repetition"""
print(tup1*3)
"""len"""
print(len(tup1))
"""Membership operation"""
print(3 in tup1)
print(7  not in tup1)

# Iteration : 
for i in tup:
    print(i)

# Tuple Methods : 
# index : will find the index of mentioned element 
print(tup1.index(3))
# count : will tell the frequency of elements.
print(tup1.count(3))

tup1=(1,2,3)
tup2=()
for i in tup1:
    tup2=tup2+(i,)
print(tup2)

tup=(1,)
print(tup)

# Tuple Packing and Unpacking :
"""
Tuple Packing : Assigning multiple values to a single variable.
Tuple Unpacking : Assigning values of tuple to multiple variables.
"""
tup=(1,2,3,"A",True)
a,b,c,d,e=tup
print(a)
print(b)
print(c)
print(d)
print(e)


# Conversion : 
tup=(1,2,3,4,5)
tup=list(tup)
tup[0]="A"
tup=tuple(tup)
print(tup)

# User-Defined Tuple :
n=int(input("Enter number of elements in the tuple: "))
tup=()
for i in range(n):
    ele=input(f"Enter element {i+1}: ")
    tup=tup+(ele,)
print("The user-defined tuple is:", tup)
