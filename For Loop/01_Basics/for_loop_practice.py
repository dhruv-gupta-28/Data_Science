# word="Amritsar"
# print(len(word))

# for i in range(0,len(word),1):
#     print(word[i])

# Prime Number : 
num=int(input("Enter Number : "))
for i in range(2,num):
    if num%i==0:
        print("Non-Prime Number")
        break
else:
    print("Prime Number")

print("-----------------------------------")
character=input("Enter Character : ")
print(ord(character))
val=int(input("Enter Ascii Value : ")) 
print(chr(val))       

# HelLo => hELlO
word=input("Enter Word : ")
new_word=""
for i in word:
    if i.islower():
        new_word+=i.upper()
    else:
        new_word+=i.lower()

