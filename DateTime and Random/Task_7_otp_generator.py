# Task 7: OTP Generator
# Goal: Generate a 6-digit OTP

import random

# Generate 6-digit OTP
otp = random.randint(100000, 999999)

print(f"Your 6-digit OTP: {otp}")
print("(This OTP is valid for 5 minutes)")
