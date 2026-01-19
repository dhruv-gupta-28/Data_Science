"""
Program 1: Find factorial of a number using recursion

Factorial of n (n!) = n × (n-1) × (n-2) × ... × 2 × 1
Base case: factorial(0) = 1, factorial(1) = 1
Recursive case: factorial(n) = n × factorial(n-1)
"""

def factorial(n):
    """
    Calculate factorial of a number using recursion.
    
    Args:
        n (int): Non-negative integer
        
    Returns:
        int: Factorial of n
    """
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    return n * factorial(n - 1)


# Test cases
if __name__ == "__main__":
    print("Factorial using Recursion")
    print("-" * 40)
    
    test_cases = [0, 1, 5, 7, 10]
    
    for num in test_cases:
        result = factorial(num)
        print(f"factorial({num}) = {result}")
    
    # User input example
    try:
        n = int(input("\nEnter a number to find factorial: "))
        if n < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            print(f"Factorial of {n} is {factorial(n)}")
    except ValueError:
        print("Please enter a valid integer.")
