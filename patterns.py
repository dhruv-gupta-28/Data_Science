#For Loop : 
# for i in range(start,end,step):
#     #code to be executed

# obj="Amritsar"
# for i in obj:
#     print(i)

# String --> Indexes 

# obj="Harsh"
# re=""
# for i in obj:
#     re=i+re
# print(re)

# obj="Amritsar"
# char=input("Enter The Character : ")
# for i in range(len(obj)):
#     if obj[i]==char:
#         print(f"Character {char} found at index {i}")

# # for i in range(0,5,1):
# #     print(obj[i],end="")


# # String Slicing 

"""
Pattern Printing : 

*****
*****
*****
*****
*****

rows : 5
col = 5

Outer Loop : i : Rows
Inner Loop : j : Columns 

*
**
***
****
*****

1
22
333
4444
55555

1
12
123
1234
12345

1
23
456
78910

A
BC
DEF
GHIJ
KLMNO
"""
for i in range(5):
    for j in range(5):
        print("*",end="")
    print()