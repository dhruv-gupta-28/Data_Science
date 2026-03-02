"""
Recursion: Countdown

Simple countdown example demonstrating basic recursive concept.
Recursion: A function that calls itself with a smaller problem.
"""


def countdown(n: int) -> None:
    """
    Count down from n to 1 recursively.
    
    Args:
        n: Starting number
        
    Returns:
        None
    """
    if n == 0:  # Base case
        print("Done!")
    else:
        print(n)
        countdown(n - 1)  # Recursive case


if __name__ == "__main__":
    print("Countdown from 5:")
    countdown(5)
