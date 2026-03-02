"""
DateTime and Random: Advanced Patterns
=======================================

Topics Covered:
- Complex datetime calculations
- Recurring events and scheduling
- Interval periods
- Random distributions
- Weighted random selection
- Simulation patterns
"""

import datetime
import random
import statistics

# ============================================================================
# 1. ADVANCED DATETIME CALCULATIONS
# ============================================================================

print("--- Advanced DateTime Calculations ---")

# Working with time deltas
start_date = datetime.date(2024, 1, 1)
end_date = datetime.date(2024, 12, 31)

duration = end_date - start_date
print(f"Days in 2024: {duration.days}")

# Calculate weeks and remaining days
weeks = duration.days // 7
days = duration.days % 7
print(f"In weeks: {weeks} weeks, {days} days")

# Time delta arithmetic
current = datetime.datetime.now()
one_week_later = current + datetime.timedelta(weeks=1)
one_month_later = current + datetime.timedelta(days=30)
print(f"One week later: {one_week_later.date()}")

# ============================================================================
# 2. NEXT OCCURRENCE OF A DATE
# ============================================================================

print("\n--- Next Occurrence ---")

def next_occurrence(target_month, target_day):
    """Find next occurrence of a date"""
    today = datetime.date.today()
    
    # Try this year first
    try:
        next_date = datetime.date(today.year, target_month, target_day)
    except ValueError:
        # Invalid date (e.g., Feb 30)
        return None
    
    # If already passed, use next year
    if next_date < today:
        next_date = datetime.date(today.year + 1, target_month, target_day)
    
    days_left = (next_date - today).days
    return next_date, days_left

# Christmas
christmas, days = next_occurrence(12, 25)
print(f"Next Christmas: {christmas} ({days} days away)")

# ============================================================================
# 3. RECURRING EVENTS
# ============================================================================

print("\n--- Recurring Events ---")

def generate_occurrences(start_date, interval_days, num_occurrences):
    """Generate recurring event dates"""
    occurrences = []
    current = start_date
    
    for _ in range(num_occurrences):
        occurrences.append(current)
        current += datetime.timedelta(days=interval_days)
    
    return occurrences

# Weekly meetings starting March 1st
start = datetime.date(2024, 3, 1)
meetings = generate_occurrences(start, 7, 5)
print("Weekly meetings:")
for meeting in meetings:
    print(f"  {meeting.strftime('%A, %B %d, %Y')}")

# ============================================================================
# 4. BUSINESS DAYS CALCULATION
# ============================================================================

print("\n--- Business Days ---")

def count_business_days(start, end):
    """Count business days (Mon-Fri) in range"""
    count = 0
    current = start
    
    while current <= end:
        # Monday=0, Sunday=6
        if current.weekday() < 5:  # 0-4 are Mon-Fri
            count += 1
        current += datetime.timedelta(days=1)
    
    return count

start = datetime.date(2024, 3, 1)
end = datetime.date(2024, 3, 31)
biz_days = count_business_days(start, end)
print(f"Business days in March 2024: {biz_days}")

# ============================================================================
# 5. RANDOM DISTRIBUTIONS
# ============================================================================

print("\n--- Random Distributions ---")

# Uniform distribution
uniform = [random.uniform(0, 100) for _ in range(5)]
print(f"Uniform (0-100): {[round(x, 2) for x in uniform]}")

# Normal distribution
normal = [random.gauss(100, 15) for _ in range(5)]
print(f"Normal (mean=100, std=15): {[round(x, 2) for x in normal]}")

# Generate histogram of distribution
print("\nNormal distribution histogram:")
data = [random.gauss(0, 1) for _ in range(1000)]
for i in range(-3, 4):
    count = sum(1 for x in data if i <= x < i+1)
    bar = '*' * (count // 10)
    print(f"  {i}: {bar}")

# ============================================================================
# 6. WEIGHTED RANDOM SELECTION
# ============================================================================

print("\n--- Weighted Random Selection ---")

# Random choice with weights
fruits = ['Apple', 'Banana', 'Cherry', 'Date']
weights = [50, 30, 15, 5]  # Apple most common

choices = [random.choices(fruits, weights=weights, k=1)[0] for _ in range(20)]
print(f"Weighted selection (20 samples): {choices}")

# Count frequencies
from collections import Counter
frequencies = Counter(choices)
print(f"Frequencies: {dict(frequencies)}")

# ============================================================================
# 7. RANDOM DATETIME GENERATOR
# ============================================================================

print("\n--- Random DateTime Generator ---")

def random_datetime_in_range(start, end):
    """Generate random datetime between two datetimes"""
    time_diff = end - start
    random_seconds = random.randint(0, int(time_diff.total_seconds()))
    return start + datetime.timedelta(seconds=random_seconds)

start_dt = datetime.datetime(2024, 1, 1)
end_dt = datetime.datetime(2024, 12, 31)

random_dates = [random_datetime_in_range(start_dt, end_dt) for _ in range(5)]
print("Random dates in 2024:")
for dt in random_dates:
    print(f"  {dt.strftime('%Y-%m-%d %H:%M:%S')}")

# ============================================================================
# 8. MONTE CARLO SIMULATION
# ============================================================================

print("\n--- Monte Carlo Simulation ---")

def estimate_pi(num_samples):
    """Estimate PI using Monte Carlo method"""
    inside_circle = 0
    
    for _ in range(num_samples):
        x = random.random()
        y = random.random()
        
        if x*x + y*y <= 1:
            inside_circle += 1
    
    return 4 * inside_circle / num_samples

pi_estimate = estimate_pi(100000)
print(f"Estimated PI: {pi_estimate}")
print(f"Actual PI: {3.141592653589793}")
print(f"Error: {abs(pi_estimate - 3.141592653589793):.6f}")

# ============================================================================
# 9. BIRTHDAY PARADOX SIMULATION
# ============================================================================

print("\n--- Birthday Paradox ---")

def birthday_paradox(group_size, num_simulations):
    """Simulate birthday paradox"""
    matches = 0
    
    for _ in range(num_simulations):
        birthdays = [random.randint(1, 365) for _ in range(group_size)]
        if len(birthdays) != len(set(birthdays)):  # Collision detected
            matches += 1
    
    probability = matches / num_simulations
    return probability

for size in [23, 50, 100]:
    prob = birthday_paradox(size, 10000)
    print(f"  Group of {size}: {prob:.2%} probability of shared birthday")

# ============================================================================
# 10. RANDOM WALK SIMULATION
# ============================================================================

print("\n--- Random Walk Simulation ---")

def random_walk_1d(steps):
    """1D random walk"""
    position = 0
    positions = [0]
    
    for _ in range(steps):
        position += random.choice([-1, 1])
        positions.append(position)
    
    return positions

# Simulate random walks
walks = [random_walk_1d(100) for _ in range(5)]
print("Random walk 1D (5 simulations, 100 steps):")
for i, walk in enumerate(walks):
    print(f"  Walk {i+1}: final position = {walk[-1]}")

# ============================================================================
# 11. PRACTICE PROBLEMS
# ============================================================================

print("\n--- Practice Problems ---")

# Problem 1: Schedule generator
print("\nProblem 1: Event Scheduler")
def schedule_events(start_date, num_events, min_gap_days):
    """Schedule events with minimum days between"""
    events = [start_date]
    current = start_date
    
    for _ in range(num_events - 1):
        gap = random.randint(min_gap_days, min_gap_days + 10)
        current += datetime.timedelta(days=gap)
        events.append(current)
    
    return events

events = schedule_events(datetime.date(2024, 3, 1), 5, 7)
print("Scheduled events:")
for event in events:
    print(f"  {event}")

# Problem 2: Statistical analysis of distribution
print("\nProblem 2: Distribution Analysis")
def analyze_distribution(samples):
    """Analyze random distribution"""
    return {
        'mean': statistics.mean(samples),
        'median': statistics.median(samples),
        'stdev': statistics.stdev(samples),
        'min': min(samples),
        'max': max(samples)
    }

samples = [random.gauss(100, 15) for _ in range(100)]
stats = analyze_distribution(samples)
print(f"Stats: mean={stats['mean']:.2f}, median={stats['median']:.2f}, stdev={stats['stdev']:.2f}")

# ============================================================================
# 12. CHALLENGES
# ============================================================================

print("\n--- Challenges ---")

# Challenge 1: Birthday scheduler
print("\nChallenge 1: Birthday Calendar")
# TODO: Create a system to track and remind about upcoming birthdays

# Challenge 2: Appointment scheduler
print("\nChallenge 2: Conflict-Free Scheduler")
# TODO: Schedule appointments avoiding conflicts with existing calendar

# Challenge 3: Lottery simulator
print("\nChallenge 3: Lottery Analyzer")
# TODO: Simulate lottery drawings and analyze probability patterns
