# 45. A simple quiz with one question and multiple-choice answers.

print("What is the capital of France?")
print("a) Berlin")
print("b) Madrid")
print("c) Paris")
print("d) Rome")

answer = input("Enter your choice (a, b, c, or d): ").lower()

if answer == "c":
    print("Correct! You are a genius.")
else:
    print("Incorrect. The correct answer is Paris.")