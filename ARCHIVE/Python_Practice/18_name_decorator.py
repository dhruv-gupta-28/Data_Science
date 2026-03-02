def name_printer(func):
    def wrapper():
        print("Antigravity Wrapper") # Printing name as requested (interpreting as decorator prints something)
        func()
    return wrapper

@name_printer
def sample():
    print("Inside sample function")

if __name__ == "__main__":
    sample()
