def my_decorator(func):
    def wrapper():
        print("Decorator is running")
        func()
    return wrapper

@my_decorator
def display():
    print("Display function running")

if __name__ == "__main__":
    display()
