"""
Recursion: Factorial

Calculate factorial using recursion.
n! = n × (n-1) × (n-2) × ... × 1
"""


def factorial(n: int) -> int:
    """
    Calculate factorial recursively.
    
    Args:
        n: Number to calculate factorial for
        
    Returns:
        Factorial of n
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    
    if n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case


if __name__ == "__main__":
    print("Factorial examples:")
    print(f"5! = {factorial(5)}")
    print(f"6! = {factorial(6)}")
    print(f"10! = {factorial(10)}")
