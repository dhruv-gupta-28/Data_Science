def simple_decorator(func):
    def wrapper():
        print("Hello from decorator")
        func()
    return wrapper

def greet():
    print("Greeting from function")

if __name__ == "__main__":
    # Applying manually to show understanding (though @ is typical)
    decorated_greet = simple_decorator(greet)
    decorated_greet()
