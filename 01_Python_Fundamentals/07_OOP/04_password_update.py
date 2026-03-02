class UserAccount:
    def __init__(self, password):
        # Initialize directly to _password to avoid validation or use setter? 
        # "Create an object with password 'hello12'" implies it should succeed.
        # We will use the setter logic to be consistent, but we need to initialize the property.
        self._password = None
        self.password = password

    def set_password(self, value):
        if len(value) >= 6:
            self._password = value
        else:
            print("Password too short") # Assuming we want feedback on rejection

    password = property(fset=set_password)

    def check_password(self, value):
        return self._password == value

# Test Code
if __name__ == "__main__":
    print("Creating user with password 'hello12'...")
    user = UserAccount("hello12")
    
    print("Updating password to 'secure99'...")
    user.password = "secure99"
    
    print("Trying to update password to '123'...")
    user.password = "123" 
    
    print(f"Check 'secure99': {user.check_password('secure99')}")
    print(f"Check '123': {user.check_password('123')}")
