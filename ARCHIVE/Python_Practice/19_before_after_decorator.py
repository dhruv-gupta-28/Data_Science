def around_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

@around_decorator
def core_function():
    print(">>> CORE FUNCTION <<<")

if __name__ == "__main__":
    core_function()
