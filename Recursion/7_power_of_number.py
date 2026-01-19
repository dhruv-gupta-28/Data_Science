"""
Program 7: Find power of a number (xⁿ) using recursion

xⁿ = x × x × ... × x (n times)
Base case: x⁰ = 1, x¹ = x
Recursive case: xⁿ = x × x^(n-1)

Optimized version: xⁿ = (x^(n/2))² if n is even
                   xⁿ = x × (x^((n-1)/2))² if n is odd
"""

def power(x, n):
    """
    Calculate x raised to the power n using recursion.
    
    Args:
        x (float): Base number
        n (int): Exponent (non-negative integer)
        
    Returns:
        float: x raised to the power n
    """
    # Base cases
    if n == 0:
        return 1
    if n == 1:
        return x
    if n < 0:
        return 1 / power(x, -n)  # Handle negative exponents
    
    # Recursive case
    return x * power(x, n - 1)


def power_optimized(x, n):
    """
    Calculate x raised to the power n using optimized recursion.
    Time complexity: O(log n) instead of O(n)
    
    Args:
        x (float): Base number
        n (int): Exponent (non-negative integer)
        
    Returns:
        float: x raised to the power n
    """
    # Base cases
    if n == 0:
        return 1
    if n == 1:
        return x
    if n < 0:
        return 1 / power_optimized(x, -n)
    
    # Optimized recursive case
    if n % 2 == 0:
        # If n is even: xⁿ = (x^(n/2))²
        half_power = power_optimized(x, n // 2)
        return half_power * half_power
    else:
        # If n is odd: xⁿ = x × (x^((n-1)/2))²
        half_power = power_optimized(x, (n - 1) // 2)
        return x * half_power * half_power


# Test cases
if __name__ == "__main__":
    print("Power of a Number using Recursion")
    print("-" * 40)
    
    test_cases = [
        (2, 0), (2, 1), (2, 5), (2, 10),
        (3, 4), (5, 3),
        (2, -3),  # Negative exponent
        (10, 0)
    ]
    
    print("\nBasic Recursion:")
    for x, n in test_cases:
        result = power(x, n)
        print(f"{x}^{n} = {result}")
    
    print("\nOptimized Recursion (O(log n)):")
    for x, n in test_cases:
        result = power_optimized(x, n)
        print(f"{x}^{n} = {result}")
    
    # User input example
    try:
        x = float(input("\nEnter base (x): "))
        n = int(input("Enter exponent (n): "))
        result = power_optimized(x, n)
        print(f"{x}^{n} = {result}")
    except ValueError:
        print("Please enter valid numbers.")
