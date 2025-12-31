# 12. Check if a password is valid (must be at least 8 characters).

password = input("Enter your password: ")

if len(password) >= 8:
    print("Password is valid.")
else:
    print("Password is invalid. It must be at least 8 characters long.")