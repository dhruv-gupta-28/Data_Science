"""
Recursion: Sum of Numbers

Calculate sum of all numbers from 1 to n recursively.
sum(5) = 1 + 2 + 3 + 4 + 5 = 15
"""


def sum_recursive(n: int) -> int:
    """
    Sum all numbers from 1 to n recursively.
    
    Args:
        n: Upper limit for sum
        
    Returns:
        Sum of numbers 1 to n
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Cannot sum negative range")
    
    if n == 0:
        return 0
    else:
        return n + sum_recursive(n - 1)


if __name__ == "__main__":
    print("Sum examples:")
    print(f"Sum of 1 to 5: {sum_recursive(5)}")
    print(f"Sum of 1 to 10: {sum_recursive(10)}")
    print(f"Sum of 1 to 100: {sum_recursive(100)}")
