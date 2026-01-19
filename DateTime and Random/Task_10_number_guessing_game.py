# Task 10: Number Guessing Game
# Goal:
# - Computer chooses random number (1–100)
# - User keeps guessing until correct
# - Count attempts

import random

# Computer chooses a random number
secret_number = random.randint(1, 100)
attempts = 0

print("🎯 Number Guessing Game 🎯")
print("I'm thinking of a number between 1 and 100.")
print("-" * 40)

while True:
    # Get user's guess
    guess = int(input("Enter your guess: "))
    attempts += 1
    
    # Check the guess
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"\n🎉 Congratulations! You guessed it in {attempts} attempts!")
        print(f"The number was {secret_number}")
        break
