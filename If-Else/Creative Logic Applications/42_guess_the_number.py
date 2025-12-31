# 42. A number guessing game where the user has one chance.

import random

secret_number = random.randint(1, 10)

guess = int(input("Guess a number between 1 and 10: "))

if guess == secret_number:
    print("Congratulations! You guessed it right.")
else:
    print(f"Sorry, the number was {secret_number}. Better luck next time!")