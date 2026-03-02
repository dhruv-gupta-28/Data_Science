def post_decorator(func):
    def wrapper():
        func()
        print("Function finished")
    return wrapper

@post_decorator
def task():
    print("Executing task logic...")

if __name__ == "__main__":
    task()
