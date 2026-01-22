"""
-Statement : execute once
-loops : executes till the condition is true. ||Iterator
    -for
    -while
    -do-while does not exist.

    for loop : 
    range(start,end,step)
"""
# num=int(input("Enter Number : "))
# for i in range(1,11,1):
#     print(f"{num} X {i} = {num*i}")


# word="Amritsar"
# for i in word:
#     print(i)

# for i in range(len(word)):
#     print(word[i])


# Break and Continue 
"""
Break : Stops the iteration
continue : skips the iteration
"""
# for i in range(10):
#     print(i)
#     if i==6:
#         break
# for i in range(10):
#     if i==6:
#         continue
#     print(i)

# num=int(input("Enter Number : "))
# for i in range(2,num):
#     if num%i==0:
#         print("Non-Prime Number")
#         break
# else:
#         print("Prime Number")

# Fibonacci Series
n=int(input("Enter Number of Terms : "))
a=0
b=1
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b
    # c=a+b
    # a=b
    # b=c

