# Task 6: Dice Game
# Goal: Roll a dice (1–6) and print result.
# Bonus: Allow user to roll again.

import random

print("🎲 Dice Game 🎲")
print("-" * 30)

while True:
    # Roll the dice
    dice_result = random.randint(1, 6)
    print(f"Dice rolled: {dice_result}")
    
    # Ask if user wants to roll again
    roll_again = input("\nRoll again? (yes/no): ").lower()
    if roll_again != 'yes':
        print("Thanks for playing!")
        break
    print()
