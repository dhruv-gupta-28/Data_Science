"""
pattern to be printed:
*
**
***
****
*****
"""

#using nested for loop
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

#using single for loop
for i in range(5):
    print("*" * (i+1))


"""
pattern to be printed:
1
22
333
4444
55555
"""
for i in range(1, 6):
    for j in range(i):
        print(i, end="")
    print()


"""
pattern to be printed:
1
12
123
1234
12345
"""

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()


"""
pattern to be printed:
1
23
456
78910
"""
num = 1
for i in range(1, 5):
    for j in range(i):
        print(num, end="")
        num += 1
    print()

"""
pattern to be printed:
A
B C
D E F
G H I J
K L M N O
"""

char = ord('A')
for i in range(1, 6):
    for j in range(i):
        print(chr(char), end=" ")
        char += 1
    print()

# Descending pattern
"""
    *****
    ****
    ***
    **
    *

    54321
    5432
    543
    54
    5
"""

for i in range(5,0,-1):
    for j in range(0,i,1):
        print(i,end="")
    print()


"""
54321
5432
543
54
5
"""
print()
for i in range(5,0,-1):
    num=5
    for j in range(i):
        print(num,end="")
        num-=1
    print()
print()

num=15
for i in range(5,0,-1):
    # num=5
    for j in range(i):
        print(num,end="")
        num-=1
    print()


"""
     *
    * *
   * * *
  * * * *
 * * * * *

"""

for i in range(5):
    for k in range(5-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("* ",end="")
    print()

"""
Pattern to be printed:

    *
   * *
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *
"""

for i in range(10):
    if i<5:
        for k in range(5-i-1):
            print(" ",end="")
        for j in range(i+1):
            print("* ",end="")
        print()
    if i >5:
        for k in range(i-5):
            print(" ",end="")
        for j in range(10-i):
            print("* ",end="")
        print()
    else:
        pass

"""
* * * * *
*       *
*       *
*       *  
* * * * *
"""

n=5
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

"""
Pattern to be printed: Circle 
"""
n=7
for i in range(n):
    for j in range(n):
        dist=((i-(n//2))**2+(j-(n//2))**2)**0.5
        if dist>2.5 and dist<3.5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

"""
Pattern to be printed: hollow diamond
     *
    * *
   *   *
  *     *
 *       *
*         *
 *       *
  *     *
   *   *
    * *
     *
"""
n=11
for i in range(n):
    for j in range(n):
        if abs(n//2 - i) + abs(n//2 - j) == n//2:
            print("*", end="")
        else:
            print(" ", end="")
    print()


"""
Pattern to be printed: DHRUV using *
"""
n = 7
for i in range(n):
    # D
    for j in range(n):
        if j == 0 or (i == 0 and j < n - 1) or (i == n - 1 and j < n - 1) or (j == n - 1 and 0 < i < n - 1):
            print("*", end="")
        else:
            print(" ", end="")
    print("  ", end="")

    # H
    for j in range(n):
        if j == 0 or j == n - 1 or i == n // 2:
            print("*", end="")
        else:
            print(" ", end="")
    print("  ", end="")

    # R
    for j in range(n):
        if j == 0 or (i == 0 and j < n - 1) or (i == n // 2 and j < n - 1) or (j == n - 1 and 0 < i < n // 2) or (i > n // 2 and j == i - n // 2):
            print("*", end="")
        else:
            print(" ", end="")
    print("  ", end="")

    # U
    for j in range(n):
        if (j == 0 and i < n - 1) or (j == n - 1 and i < n - 1) or (i == n - 1 and 0 < j < n - 1):
            print("*", end="")
        else:
            print(" ", end="")
    print("  ", end="")

    # V (meets at the middle row)
    for j in range(n*2 -1):
        if i <= (n - (1/2)) and (j == i or j == n*2 - 2 - i):
            print("*", end="")
        else:
            print(" ", end="")

    print()