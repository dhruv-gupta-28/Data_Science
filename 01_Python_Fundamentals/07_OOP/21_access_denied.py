def block_access(func):
    def wrapper(*args, **kwargs):
        print("Access denied")
        # Function is NOT called
    return wrapper

@block_access
def sensitive_data():
    print("This is secret data!")

if __name__ == "__main__":
    print("Attempting to access sensitive data...")
    sensitive_data()
