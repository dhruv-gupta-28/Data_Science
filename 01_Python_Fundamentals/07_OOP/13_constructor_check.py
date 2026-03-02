class Check:
    def __init__(self):
        print("Constructor Executed!")

if __name__ == "__main__":
    print("Creating first object...")
    obj1 = Check()
    
    print("Creating second object...")
    obj2 = Check()
    
    print("If 'Constructor Executed!' printed twice, the constructor ran twice.")
