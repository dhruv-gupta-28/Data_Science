def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with args: {args}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

if __name__ == "__main__":
    print("Adding 5 and 7:")
    add(5, 7)
