# Dictionary : 
"""
Dictionary is a non primitive data type which stores the value in the pair of key and 
value .
It is also Heterogenous in Nature. 
It is Denoted bby "{}" .

syntax : 
    dict1={
        'Key' : 'Value',
        'Key' : 'Value'
    }

Features : 
-Unordered 
-Mutable
-Dont Allow Duplicacy 
"""

# Declaring a dictionary : 
emp1={
    'Name':"Harsh",
    'age':23,
    'city':"Dewas"
}
print(emp1)
print(type(emp1))

# Particular Key Access : 
print(emp1["Name"])

# Mutablity : 
emp1["Name"]="Rohit"
print(emp1)

# Add a Key : 
"""
variable_name["New_key"]=new_value
"""
emp1["Profile"]="Java Dev."
print(emp1)
print(emp1["Profile"])

# Does not allow duplicacy : 
emp1={
    'Name':"Harsh",
    'age':23,
    'city':"Dewas",
    'age':33
}
print(emp1)

# Delete a key :
emp1={
    'Name':"Harsh",
    'age':23,
    'city':"Dewas",
    'Profile':"Python Dev"
} 
del emp1["Profile"]
print(emp1)

# How Can we Merge a Dictionary :
dict1={
    "Name":"Harsh",
    "Age":13
}
dict2={
    "City":"Indore",
    "Class":7
}
print(dict1|dict2)      #Concatination Using Pipe Operator

# Iteration : 
emp1={
    'Name':"Harsh",
    'age':23,
    'city':"Dewas"
}
for i in emp1:
    print(f"{i} : {emp1[i]}")
for i,j in emp1.items() :
    print(i,j)

# Dictionary Methods : 
print(emp1.get("Name"))
print(emp1.keys())
print(emp1.values())
print(emp1.items())
emp1.update({'Name':"Kunal"})
print(emp1)
emp1.clear()
print(emp1)

# Nested Dictionary : 
"""
Dictionary declared inside a dictionary is known as Nested Dictionary .
"""
dict1={
    'name':["Harsh","Amit","Rahul"],
    'Age':[21,22,23]
}
comp={
    "emp1":{
        'Name':"Harsh",
        "age":23,
        "city":"Pune"
    },
    "emp2":{
        'Name':"Harshit",
        "age":26,
        "city":"Dewas"
    },
    "emp3":{
        'Name':"Harshita",
        "age":25,
        "city":"Nagpur"
    },
    "emp4":{
        'Name':"Harish",
        "age":25,
        "city":"Delhi"
    },
}
# print(comp)
print(comp["emp1"]["Name"])


# User-Defined Dictionary : 
# tot=int(input("Enter Number of Key's : "))
# dict1={}
# for i in range(tot):
#     key=input(f"Enter  Key {i+1}: ")
#     value=input(f"Enter  Value {i+1} :")
#     dict1[key]=value
# print(dict1)


tot=int(input("Enter Number of Key's : "))
dict1={}
for i in range(tot):
    key=input(f"Enter  Key {i+1}: ")
    tot2=int(input("Enter Total Key's : "))
    val={}
    for j in range(tot2):
        child_key=input("Enter Child Key : ")
        child_value=input("Enter Child Value : ")
        val[child_key]=child_value
    dict1[key]=val
print(dict1)

# Dictionary Comprehension : 
"""
Syntax : 
dict1={key:expression for i in range() conditional}
"""
dict1={i:i**2 for i in range(1,11) if i%2==0}
print(dict1)
li=[1,2,3]
dict2={i:i*2 for i in li}
print(dict2)