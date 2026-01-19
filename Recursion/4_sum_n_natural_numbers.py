"""
Program 4: Find the sum of first N natural numbers using recursion

Sum of first N natural numbers = 1 + 2 + 3 + ... + N = N(N+1)/2
Base case: sum(0) = 0, sum(1) = 1
Recursive case: sum(n) = n + sum(n-1)
"""

def sum_natural_numbers(n):
    """
    Calculate sum of first n natural numbers using recursion.
    
    Args:
        n (int): Number of natural numbers to sum
        
    Returns:
        int: Sum of first n natural numbers
    """
    # Base case
    if n <= 0:
        return 0
    if n == 1:
        return 1
    # Recursive case
    return n + sum_natural_numbers(n - 1)


# Test cases
if __name__ == "__main__":
    print("Sum of First N Natural Numbers using Recursion")
    print("-" * 40)
    
    test_cases = [0, 1, 5, 10, 100]
    
    for n in test_cases:
        result = sum_natural_numbers(n)
        formula_result = n * (n + 1) // 2  # Verification using formula
        print(f"Sum of first {n} natural numbers = {result} (verified: {formula_result})")
    
    # User input example
    try:
        n = int(input("\nEnter a number N: "))
        if n < 0:
            print("Please enter a non-negative number.")
        else:
            result = sum_natural_numbers(n)
            print(f"Sum of first {n} natural numbers = {result}")
    except ValueError:
        print("Please enter a valid integer.")
