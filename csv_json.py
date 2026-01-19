"""
CSV : Comma-Separated Values
eg : 
name,age,city
Alice,30,New York   
Bob,25,Los Angeles


JSON : JavaScript Object Notation
eg :
[
  {
    "name": "Alice",
    "age": 30,
    "city": "New York"
  },
  {
    "name": "Bob",
    "age": 25,
    "city": "Los Angeles"
  }
]
"""
import csv
"""
Modes in CSv :
r : read
w : write
a : append
"""
# f=open('data.csv', 'r')
# data=csv.reader(f)
# for i in data:
#     print(i)  # each row is represented as a list
# f.close()

# Using DictReader
# f=open('data.csv', 'r')
# data=csv.DictReader(f)
# for i in data:
#     print(i)  # each row is represented as a dictionary
# f.close()

# Writing into CSV
# f=open('data_write.csv', 'w', newline='')
# data=csv.writer(f)
# tot=int(input("Enter number of rows to write : "))
# for i in range(tot):
#     name=input("Enter name : ")
#     age=input("Enter age : ")
#     city=input("Enter city : ")
#     data.writerow([name, age, city])
# f.close()

# Using DictWriter
# f=open('data_dictwrite.csv', 'w', newline='')
# data=csv.DictWriter(f, fieldnames=['name', 'age', 'city'])
# data.writeheader()
# data.writerow({'name': 'John', 'age': 28, 'city': 'Chicago'})
# tot=int(input("Enter number of rows to write : "))
# for i in range(tot):
#     name=input("Enter name : ")
#     age=input("Enter age : ")
#     city=input("Enter city : ")
#     data.writerow({'name': name, 'age': age, 'city': city})
# f.close()

# Append using with statement
# with open('data_append.csv', 'a', newline='') as f:
#     data=csv.writer(f)
#     tot=int(input("Enter number of rows to append : "))
#     for i in range(tot):
#         name=input("Enter name : ")
#         age=input("Enter age : ")
#         city=input("Enter city : ")
#         data.writerow([name, age, city])

"""
Parameters in csv.writer() and csv.DictWriter()
delimiter : character that separates values (default is comma)
quotechar : character used to quote fields containing special characters (default is double quote)

extrasaction : specifies what to do with extra fields not defined in fieldnames (for DictWriter)
restval : specifies the default value for missing fields (for DictWriter)
"""

import json
# Reading JSON file
f=open('data.json', 'r')
data=json.load(f)
print(data)
f.close()

# Writing JSON file
f=open('data_write.json', 'w')
data_to_write=[
    {"name": "Charlie", "age": 35, "city": "San Francisco"},
    {"name": "Diana", "age": 28, "city": "Miami"}
]