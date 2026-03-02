"""
Recursion: Fibonacci Sequence

Calculate nth Fibonacci number using recursion.
Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...
"""


def fibonacci(n: int) -> int:
    """
    Calculate nth Fibonacci number recursively.
    
    Args:
        n: Position in Fibonacci sequence (0-indexed)
        
    Returns:
        The nth Fibonacci number
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Fibonacci index cannot be negative")
    
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    print("Fibonacci sequence:")
    for i in range(8):
        print(f"fib({i}) = {fibonacci(i)}")
