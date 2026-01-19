# Task 12: Daily Quote Generator
# Goal:
# - Store 10 quotes in a list
# - Show one random quote per day
# - Same quote should repeat if same day

import random
from datetime import datetime

# List of quotes
quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Innovation distinguishes between a leader and a follower. - Steve Jobs",
    "Life is what happens to you while you're busy making other plans. - John Lennon",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "It is during our darkest moments that we must focus to see the light. - Aristotle",
    "The only impossible journey is the one you never begin. - Tony Robbins",
    "In the middle of difficulty lies opportunity. - Albert Einstein",
    "The way to get started is to quit talking and begin doing. - Walt Disney",
    "Don't let yesterday take up too much of today. - Will Rogers",
    "You learn more from failure than from success. - Unknown"
]

# Get today's date
today = datetime.now().date()

# Use date as seed for random (ensures same quote for same day)
random.seed(today.toordinal())

# Select a quote
daily_quote = random.choice(quotes)

print("📖 Daily Quote")
print("-" * 50)
print(f"Date: {today.strftime('%Y-%m-%d')}")
print(f"\n{daily_quote}")
print("-" * 50)
