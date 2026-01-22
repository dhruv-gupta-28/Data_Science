"""
14. Write code where:
    - class variable `counter`
    - increment it every time an object is created
    - create 4 objects and print counter
"""

class Item:
    counter = 0

    def __init__(self):
        Item.counter += 1

if __name__ == "__main__":
    o1 = Item()
    o2 = Item()
    o3 = Item()
    o4 = Item()
    
    print(f"Final Counter Value: {Item.counter}")
