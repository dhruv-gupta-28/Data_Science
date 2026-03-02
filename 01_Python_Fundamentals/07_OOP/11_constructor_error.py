class Example:
    def __init__(self, value):
        self.value = value

if __name__ == "__main__":
    print("Attempting to create object without arguments (constructor expects one)...")
    try:
        # This triggers TypeError: __init__() missing 1 required positional argument: 'value'
        obj = Example() 
    except TypeError as e:
        print(f"Caught expected error: {e}")
