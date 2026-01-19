# Task 8: Lucky Draw Program
# Goal: Given a list of names → randomly select one winner

import random

# List of participants
participants = []
print("Enter participant names (type 'done' when finished):")

while True:
    name = input("Enter name: ").strip()
    if name.lower() == 'done':
        break
    if name:
        participants.append(name)

if participants:
    print(f"\nParticipants: {participants}")
    winner = random.choice(participants)
    print(f"\n🎉 Winner: {winner} 🎉")
else:
    print("No participants entered.")
