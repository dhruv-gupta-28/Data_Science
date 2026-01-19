"""
Program 15: Calculate GCD of two numbers using recursion

GCD (Greatest Common Divisor) using Euclidean Algorithm:
- Base case: If b == 0, return a
- Recursive case: GCD(a, b) = GCD(b, a % b)

Euclidean Algorithm is based on the principle that:
GCD(a, b) = GCD(b, a mod b)
"""

def gcd(a, b):
    """
    Calculate GCD of two numbers using recursion (Euclidean Algorithm).
    
    Args:
        a (int): First number
        b (int): Second number
        
    Returns:
        int: GCD of a and b
    """
    # Handle negative numbers
    a, b = abs(a), abs(b)
    
    # Ensure a >= b
    if a < b:
        a, b = b, a
    
    # Base case
    if b == 0:
        return a
    
    # Recursive case: Euclidean Algorithm
    return gcd(b, a % b)


# Test cases
if __name__ == "__main__":
    print("GCD (Greatest Common Divisor) using Recursion")
    print("-" * 40)
    
    test_cases = [
        (48, 18),
        (56, 42),
        (100, 25),
        (17, 13),
        (60, 48),
        (0, 5),
        (5, 0),
        (1, 1),
        (100, 1)
    ]
    
    for a, b in test_cases:
        result = gcd(a, b)
        print(f"GCD({a}, {b}) = {result}")
    
    # User input example
    try:
        a = int(input("\nEnter first number: "))
        b = int(input("Enter second number: "))
        result = gcd(a, b)
        print(f"GCD({a}, {b}) = {result}")
    except ValueError:
        print("Please enter valid integers.")
