# Task 11: Quiz App
# Goal:
# - Ask 5 random questions
# - Track start & end time
# - Show total time taken

import random
from datetime import datetime

# Quiz questions and answers
questions = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is 2 + 2?", "answer": "4"},
    {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
    {"question": "What is the chemical symbol for water?", "answer": "H2O"},
    {"question": "Who wrote Romeo and Juliet?", "answer": "Shakespeare"},
    {"question": "What is the square root of 64?", "answer": "8"},
    {"question": "What is the smallest prime number?", "answer": "2"},
    {"question": "What is the capital of Japan?", "answer": "Tokyo"},
    {"question": "How many continents are there?", "answer": "7"},
    {"question": "What is the speed of light?", "answer": "299792458"}
]

# Select 5 random questions
selected_questions = random.sample(questions, 5)

# Record start time
start_time = datetime.now()
print("📝 Quiz Started!")
print("-" * 40)

score = 0
for i, q in enumerate(selected_questions, 1):
    print(f"\nQuestion {i}: {q['question']}")
    user_answer = input("Your answer: ").strip()
    
    if user_answer.lower() == q['answer'].lower():
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer: {q['answer']}")

# Record end time
end_time = datetime.now()
total_time = (end_time - start_time).total_seconds()

print("\n" + "=" * 40)
print(f"Quiz completed!")
print(f"Score: {score}/5")
print(f"Total time taken: {total_time:.2f} seconds")
