"""
5. Write a program where:
   - a class variable counts number of objects created
   - print the final count
"""

class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

if __name__ == "__main__":
    obj1 = Counter()
    obj2 = Counter()
    obj3 = Counter()
    
    print(f"Total Objects Created: {Counter.count}")
