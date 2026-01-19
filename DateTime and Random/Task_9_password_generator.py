# Task 9: Password Generator
# Goal: Generate a strong password using:
# Uppercase, Lowercase, Numbers, Symbols

import random
import string

# Get password length from user
length = int(input("Enter password length: "))

# Define character sets
uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
digits = string.digits
symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"

# Combine all characters
all_chars = uppercase + lowercase + digits + symbols

# Ensure at least one character from each category
password = [
    random.choice(uppercase),
    random.choice(lowercase),
    random.choice(digits),
    random.choice(symbols)
]

# Fill the rest randomly
for _ in range(length - 4):
    password.append(random.choice(all_chars))

# Shuffle the password
random.shuffle(password)

# Convert to string
strong_password = ''.join(password)

print(f"Generated password: {strong_password}")
