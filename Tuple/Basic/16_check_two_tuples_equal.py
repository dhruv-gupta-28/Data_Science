# 16. Check if two tuples are equal
# Input: (1, 2, 3) and (1, 2, 3)
# Output: Tuples are equal

t1 = (1, 2, 3)
t2 = (1, 2, 3)

if len(t1) != len(t2):
    print("Tuples are not equal")
else:
    equal = True
    for i in range(len(t1)):
        if t1[i] != t2[i]:
            equal = False
            break
    
    if equal:
        print("Tuples are equal")
    else:
        print("Tuples are not equal")

