class UserAccount:
    def __init__(self):
        self._password = None

    # Using property() manually to create a write-only-ish property behavior 
    # (or just a setter without an exposed getter method on the class interface)
    # The requirement says "Do not create a getter".
    
    def set_password(self, value):
        if len(value) < 6:
            print("Password too short")
        else:
            self._password = value
            
    # Defining property with only fset
    password = property(fset=set_password)

    def check_password(self, value):
        return self._password == value

# Test Code
if __name__ == "__main__":
    user = UserAccount()
    
    print("Setting password to 'secret123'...")
    user.password = "secret123"
    
    print("Trying to set short password '123'...")
    user.password = "123"
    
    print(f"Check 'secret123': {user.check_password('secret123')}")
    print(f"Check '123': {user.check_password('123')}")
