#check if all the elements in a tuple are the same 
tup = (5, 5, 5, 5)
for i in tup:
    if i != tup[0]:
        print("Not all elements are the same")
        break
else:
    print("All elements are the same")