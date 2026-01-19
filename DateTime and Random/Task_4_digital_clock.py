# Task 4: Digital Clock (Loop Based)
# Goal: Create a live digital clock that updates every second

from datetime import datetime
import time

print("Digital Clock (Press Ctrl+C to stop)")
print("-" * 30)

try:
    while True:
        # Get current time
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        
        # Clear screen and print time (works best in terminal)
        print(f"\r{current_time}", end="", flush=True)
        
        # Wait for 1 second
        time.sleep(1)
except KeyboardInterrupt:
    print("\n\nClock stopped.")
