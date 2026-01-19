"""
Program 2: Generate Fibonacci series using recursion

Fibonacci series: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
Each number is the sum of the two preceding ones.
F(0) = 0, F(1) = 1
F(n) = F(n-1) + F(n-2) for n > 1
"""

def fibonacci(n):
    """
    Calculate nth Fibonacci number using recursion.
    
    Args:
        n (int): Position in Fibonacci series (0-indexed)
        
    Returns:
        int: nth Fibonacci number
    """
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_series(n):
    """
    Generate Fibonacci series up to n terms using recursion.
    
    Args:
        n (int): Number of terms to generate
        
    Returns:
        list: List of Fibonacci numbers
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    
    # Recursively get previous series and append next term
    series = fibonacci_series(n - 1)
    series.append(series[-1] + series[-2])
    return series


# Test cases
if __name__ == "__main__":
    print("Fibonacci Series using Recursion")
    print("-" * 40)
    
    # Generate first 10 Fibonacci numbers
    print("\nFirst 10 Fibonacci numbers:")
    for i in range(10):
        print(f"F({i}) = {fibonacci(i)}")
    
    # Generate series
    print("\nFibonacci series (first 10 terms):")
    series = fibonacci_series(10)
    print(series)
    
    # User input example
    try:
        n = int(input("\nEnter number of terms to generate: "))
        if n < 0:
            print("Please enter a non-negative number.")
        else:
            series = fibonacci_series(n)
            print(f"Fibonacci series: {series}")
    except ValueError:
        print("Please enter a valid integer.")
