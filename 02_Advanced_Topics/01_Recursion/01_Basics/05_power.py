"""
Recursion: Power Function

Calculate base^exponent recursively.
"""


def power(base: int | float, exponent: int) -> int | float:
    """
    Calculate base^exponent recursively.
    
    Args:
        base: The base number
        exponent: The exponent (can be negative)
        
    Returns:
        base raised to the power of exponent
        
    Raises:
        ValueError: If base is 0 and exponent is negative
    """
    if exponent == 0:
        return 1
    elif exponent < 0:
        if base == 0:
            raise ValueError("Cannot divide by zero")
        return 1 / power(base, -exponent)
    else:
        return base * power(base, exponent - 1)


if __name__ == "__main__":
    print("Power examples:")
    print(f"2^5 = {power(2, 5)}")
    print(f"3^4 = {power(3, 4)}")
    print(f"2^(-2) = {power(2, -2)}")
    print(f"5^0 = {power(5, 0)}")
