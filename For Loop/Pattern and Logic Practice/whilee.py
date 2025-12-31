# Iterator :  repeats the condition till the logic is true .
#Statement : block of code which gets executed once .


# For Loop :
"""
Integers :
for i in range(start,end,step)
for strings : 
for i in variable :

While : 
start
while condition:
    statements
    increment
"""

# num=int(input("Enter Number : "))
# i=2
# while i<num:
#     if num%i==0:
#         print("NonPrime Number ")
#         break
#     i+=1
# else:
#     print("Prime Number")

# num=int(input("Enter Number : "))
# i,a,temp=0,0,0
# b=1
# while i<=num:
#     print(a,end=" ")
#     temp=a
#     a=b
#     b=temp+a
#     i=i+1

temp=0
num=int(input("Enter Number : "))
while num>0:
    rem=num%10
    temp=temp*10+rem
    num=num//10
    
print(temp)