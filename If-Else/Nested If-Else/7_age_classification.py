# 7. Classify a person's age as child (<13), teenager (13–19), adult (20–59), senior (60+).

age = int(input("Enter your age: "))

if age < 13:
    print("You are a child.")
else:
    if age <= 19:
        print("You are a teenager.")
    else:
        if age <= 59:
            print("You are an adult.")
        else:
            print("You are a senior.")