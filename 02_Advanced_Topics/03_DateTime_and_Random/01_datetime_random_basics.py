"""
Advanced Topics: DateTime and Random
=====================================

Topics Covered:
- datetime module basics
- Creating and manipulating dates
- Working with time objects
- Formatting dates and times
- Calculating time differences
- random module for generating random values
- Random choices and sampling
- Setting random seeds
"""

import datetime
import random
import time

# ============================================================================
# 1. DATETIME BASICS
# ============================================================================

print("--- DateTime Basics ---")

# Get current date and time
now = datetime.datetime.now()
print(f"Current datetime: {now}")
print(f"Type: {type(now)}")

# Components
print(f"\nComponents:")
print(f"  Year: {now.year}")
print(f"  Month: {now.month}")
print(f"  Day: {now.day}")
print(f"  Hour: {now.hour}")
print(f"  Minute: {now.minute}")
print(f"  Second: {now.second}")

# ============================================================================
# 2. CREATE DATE AND TIME OBJECTS
# ============================================================================

print("\n--- Create Date and Time ---")

# Create a specific date
date_obj = datetime.date(2024, 3, 15)
print(f"Date: {date_obj}")

# Create a specific time
time_obj = datetime.time(14, 30, 45)
print(f"Time: {time_obj}")

# Create a specific datetime
dt = datetime.datetime(2024, 3, 15, 14, 30, 45)
print(f"DateTime: {dt}")

# ============================================================================
# 3. DATE OPERATIONS
# ============================================================================

print("\n--- Date Operations ---")

# Today
today = datetime.date.today()
print(f"Today: {today}")

# Yesterday and tomorrow
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)
print(f"Yesterday: {yesterday}")
print(f"Tomorrow: {tomorrow}")

# Add days
future_date = today + datetime.timedelta(days=30)
print(f"30 days from now: {future_date}")

# Add weeks
next_week = today + datetime.timedelta(weeks=1)
print(f"Next week: {next_week}")

# ============================================================================
# 4. TIME DIFFERENCES
# ============================================================================

print("\n--- Time Differences ---")

date1 = datetime.date(2024, 1, 1)
date2 = datetime.date(2024, 12, 31)

difference = date2 - date1
print(f"Difference: {difference}")
print(f"Days: {difference.days}")
print(f"Total seconds: {difference.total_seconds()}")

# Calculate age
birth_date = datetime.date(2000, 5, 15)
today = datetime.date.today()
age = (today - birth_date).days // 365
print(f"Age (approx): {age} years")

# ============================================================================
# 5. FORMATTING DATES
# ============================================================================

print("\n--- Formatting Dates ---")

now = datetime.datetime.now()

# Using strftime()
print(f"Default: {now}")
print(f"ISO format: {now.isoformat()}")
print(f"Formatted (MM/DD/YYYY): {now.strftime('%m/%d/%Y')}")
print(f"Formatted (DD-Mon-YYYY): {now.strftime('%d-%b-%Y')}")
print(f"With time (MM/DD/YYYY HH:MM): {now.strftime('%m/%d/%Y %H:%M')}")
print(f"Full text: {now.strftime('%A, %B %d, %Y')}")

# Common formats
print("\nCommon format codes:")
print(f"  %Y - Year (4 digits): {now.strftime('%Y')}")
print(f"  %y - Year (2 digits): {now.strftime('%y')}")
print(f"  %m - Month (01-12): {now.strftime('%m')}")
print(f"  %d - Day (01-31): {now.strftime('%d')}")
print(f"  %H - Hour (00-23): {now.strftime('%H')}")
print(f"  %M - Minute (00-59): {now.strftime('%M')}")
print(f"  %S - Second (00-59): {now.strftime('%S')}")
print(f"  %A - Weekday name: {now.strftime('%A')}")
print(f"  %B - Month name: {now.strftime('%B')}")

# ============================================================================
# 6. PARSING DATES (PARSING STRINGS TO DATETIME)
# ============================================================================

print("\n--- Parsing Dates ---")

# Parse string to datetime
date_string = "2024-03-15 14:30:45"
parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(f"Parsed: {parsed_date}")
print(f"Type: {type(parsed_date)}")

# Other parsing examples
date_str2 = "03/15/2024"
parsed_date2 = datetime.datetime.strptime(date_str2, "%m/%d/%Y")
print(f"Parsed from MM/DD/YYYY: {parsed_date2}")

# ============================================================================
# 7. WORKING WITH TIMEZONES
# ============================================================================

print("\n--- Timezones ---")

# Naive datetime (no timezone info)
naive_dt = datetime.datetime.now()
print(f"Naive datetime: {naive_dt}")
print(f"Timezone info: {naive_dt.tzinfo}")

# UTC time
utc_now = datetime.datetime.utcnow()
print(f"UTC time: {utc_now}")

# ============================================================================
# 8. RANDOM BASICS
# ============================================================================

print("\n--- Random Basics ---")

# Random float between 0 and 1
random_float = random.random()
print(f"Random float (0-1): {random_float}")

# Random integer
random_int = random.randint(1, 100)
print(f"Random integer (1-100): {random_int}")

# Random float in range
random_range = random.uniform(10, 20)
print(f"Random float (10-20): {random_range}")

# ============================================================================
# 9. RANDOM CHOICES AND SEQUENCES
# ============================================================================

print("\n--- Random Choices ---")

# Random choice from list
colors = ['red', 'green', 'blue', 'yellow', 'purple']
chosen_color = random.choice(colors)
print(f"Random color: {chosen_color}")

# Multiple random choices
multiple = random.choices(colors, k=3)
print(f"Random 3 colors (with replacement): {multiple}")

# Unique random choices
unique = random.sample(colors, k=3)
print(f"Random 3 unique colors: {unique}")

# Shuffle a list
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(f"Shuffled list: {numbers}")

# ============================================================================
# 10. SEEDING RANDOM
# ============================================================================

print("\n--- Random Seeding ---")

# Set seed for reproducibility
random.seed(42)
print("Seeds set to 42")

# Generate random numbers
print(f"Random 1: {random.randint(1, 100)}")
print(f"Random 2: {random.randint(1, 100)}")

# Reset seed to get same sequence
random.seed(42)
print("Seed reset to 42")
print(f"Random 1: {random.randint(1, 100)}")  # Same as before
print(f"Random 2: {random.randint(1, 100)}")  # Same as before

# ============================================================================
# 11. RANDOM PRACTICAL EXAMPLES
# ============================================================================

print("\n--- Practical Examples ---")

# Dice game
print("\nDice Game:")
for roll in range(3):
    die = random.randint(1, 6)
    print(f"  Roll {roll + 1}: {die}")

# Random password generator
print("\nPassword Generator:")
import string
chars = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(chars) for _ in range(12))
print(f"  Generated password: {password}")

# Lottery numbers
print("\nLottery Numbers:")
lottery = sorted(random.sample(range(1, 50), k=6))
print(f"  Lucky numbers: {lottery}")

# Coin flip
print("\nCoin Flip:")
for _ in range(5):
    flip = random.choice(['Heads', 'Tails'])
    print(f"  {flip}")

# ============================================================================
# 12. COMBINING DATETIME AND RANDOM
# ============================================================================

print("\n--- Combining DateTime and Random ---")

# Random birthdate
def random_birthdate(start_year=1980, end_year=2005):
    """Generate random birthdate"""
    year = random.randint(start_year, end_year)
    month = random.randint(1, 12)
    day = random.randint(1, 28)  # Use 28 to avoid month-specific issues
    return datetime.date(year, month, day)

birthdate = random_birthdate()
print(f"Random birthdate: {birthdate}")

# Random datetime within a range
def random_datetime(start_year, end_year):
    """Generate random datetime"""
    year = random.randint(start_year, end_year)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    return datetime.datetime(year, month, day, hour, minute)

random_dt = random_datetime(2023, 2024)
print(f"Random datetime: {random_dt}")

# ============================================================================
# 13. ELAPSED TIME MEASUREMENT
# ============================================================================

print("\n--- Measuring Elapsed Time ---")

# Measure execution time
start_time = time.time()

# Do something
total = sum(range(1000000))

end_time = time.time()
elapsed = end_time - start_time

print(f"Sum calculation took {elapsed:.4f} seconds")

# Using datetime
start = datetime.datetime.now()
time.sleep(1)  # Sleep for 1 second
end = datetime.datetime.now()
duration = end - start
print(f"Sleep took {duration.total_seconds()} seconds")

# ============================================================================
# 14. PRACTICE PROBLEMS
# ============================================================================

print("\n--- Practice Problems ---")

# Problem 1: Days until birthday
print("\nProblem 1: Days Until Birthday")
def days_until_birthday(birth_month, birth_day):
    """Calculate days until next birthday"""
    today = datetime.date.today()
    this_year_birthday = datetime.date(today.year, birth_month, birth_day)
    
    if this_year_birthday < today:
        next_birthday = datetime.date(today.year + 1, birth_month, birth_day)
    else:
        next_birthday = this_year_birthday
    
    days_left = (next_birthday - today).days
    return days_left

days = days_until_birthday(3, 15)
print(f"Days until March 15 birthday: {days}")

# Problem 2: Random event scheduler
print("\nProblem 2: Event Scheduler")
def schedule_random_events(num_events=3):
    """Schedule random events within next 30 days"""
    today = datetime.date.today()
    events = []
    
    for i in range(num_events):
        days_offset = random.randint(0, 30)
        event_date = today + datetime.timedelta(days=days_offset)
        events.append((i + 1, event_date))
    
    return sorted(events, key=lambda x: x[1])

scheduled = schedule_random_events(3)
print("Scheduled events:")
for num, date in scheduled:
    print(f"  Event {num}: {date}")

# ============================================================================
# 15. CHALLENGES
# ============================================================================

print("\n--- Challenges ---")

# Challenge 1: Age calculator
print("\nChallenge 1: Precise Age Calculator")
# TODO: Calculate exact age in years, months, and days

# Challenge 2: Event planner
print("\nChallenge 2: Event Planner")
# TODO: Plan events with specific dates and random durations

# Challenge 3: Time zone converter
print("\nChallenge 3: Timezone Converter")
# TODO: Convert times between different timezones

# Challenge 4: Random schedule generator
print("\nChallenge 4: Schedule Generator")
# TODO: Generate random class schedule for a week with no conflicts
