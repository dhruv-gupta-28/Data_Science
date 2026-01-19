"""
Program 19: Explain LOI (Level of Indirection) in Recursion

LOI stands for "Level of Indirection" or "Line of Indirection"
It refers to the depth of recursive calls before reaching the base case.

This program demonstrates LOI with examples and visualizations.
"""

def factorial_with_loi(n, level=0):
    """
    Calculate factorial and show Level of Indirection.
    
    Args:
        n (int): Input number
        level (int): Current recursion level
        
    Returns:
        tuple: (factorial result, max level reached)
    """
    # Print indentation to show recursion depth
    indent = "  " * level
    print(f"{indent}Level {level}: factorial({n}) called")
    
    # Base case
    if n == 0 or n == 1:
        print(f"{indent}Level {level}: Base case reached, returning 1")
        return 1, level
    
    # Recursive case
    print(f"{indent}Level {level}: Calling factorial({n-1})")
    result, max_level = factorial_with_loi(n - 1, level + 1)
    final_result = n * result
    
    print(f"{indent}Level {level}: factorial({n}) = {n} * {result} = {final_result}")
    return final_result, max(max_level, level)


def fibonacci_with_loi(n, level=0, memo=None):
    """
    Calculate Fibonacci and show Level of Indirection.
    
    Args:
        n (int): Position in Fibonacci series
        level (int): Current recursion level
        memo (dict): Memoization dictionary
        
    Returns:
        tuple: (Fibonacci number, max level reached)
    """
    if memo is None:
        memo = {}
    
    indent = "  " * level
    print(f"{indent}Level {level}: fibonacci({n}) called")
    
    # Base cases
    if n == 0:
        print(f"{indent}Level {level}: Base case (n=0), returning 0")
        return 0, level
    if n == 1:
        print(f"{indent}Level {level}: Base case (n=1), returning 1")
        return 1, level
    
    # Check memoization
    if n in memo:
        print(f"{indent}Level {level}: Using memoized value for fibonacci({n})")
        return memo[n], level
    
    # Recursive case
    print(f"{indent}Level {level}: Calling fibonacci({n-1}) and fibonacci({n-2})")
    fib_n_minus_1, level1 = fibonacci_with_loi(n - 1, level + 1, memo)
    fib_n_minus_2, level2 = fibonacci_with_loi(n - 2, level + 1, memo)
    
    result = fib_n_minus_1 + fib_n_minus_2
    memo[n] = result
    
    print(f"{indent}Level {level}: fibonacci({n}) = {fib_n_minus_1} + {fib_n_minus_2} = {result}")
    return result, max(level, level1, level2)


def explain_loi():
    """
    Explain Level of Indirection with examples.
    """
    print("=" * 60)
    print("LOI (Level of Indirection) in Recursion")
    print("=" * 60)
    
    print("""
DEFINITION:
-----------
LOI (Level of Indirection) refers to the depth or number of recursive
function calls that occur before reaching the base case. It represents
how "deep" the recursion goes.

KEY CONCEPTS:
------------
1. Base Case: The condition that stops recursion (LOI = 0 at base case)
2. Recursive Case: Each call increases LOI by 1
3. Maximum LOI: The deepest level reached before returning

IMPORTANCE:
-----------
- Understanding LOI helps visualize recursion flow
- Higher LOI means more stack frames (memory usage)
- Deep recursion can lead to stack overflow
- LOI helps in debugging recursive functions

EXAMPLE 1: Factorial
--------------------
""")
    
    print("Calculating factorial(5) with LOI visualization:")
    print("-" * 60)
    result, max_level = factorial_with_loi(5)
    print(f"\nResult: {result}")
    print(f"Maximum Level of Indirection: {max_level}")
    
    print("\n" + "=" * 60)
    print("\nEXAMPLE 2: Fibonacci (showing recursion depth)")
    print("-" * 60)
    print("\nCalculating fibonacci(4) with LOI visualization:")
    print("-" * 60)
    result, max_level = fibonacci_with_loi(4)
    print(f"\nResult: {result}")
    print(f"Maximum Level of Indirection: {max_level}")
    
    print("\n" + "=" * 60)
    print("\nCOMPARISON:")
    print("-" * 60)
    print("""
Function          | Input | Max LOI | Notes
------------------|-------|---------|------------------
factorial(n)      |   n   |   n-1   | Linear recursion
fibonacci(n)      |   n   |   n-1   | Tree recursion (exponential calls)
binary_search(n)  |   n   | log(n)  | Logarithmic recursion (efficient)
tower_of_hanoi(n) |   n   |   n-1   | Each disk adds one level

OPTIMIZATION TIPS:
------------------
1. Tail Recursion: Some languages optimize tail-recursive functions
2. Memoization: Store results to avoid redundant recursive calls
3. Iterative Solutions: Convert recursion to iteration for better performance
4. Base Case Optimization: Ensure base case is reached efficiently
""")


# Test cases
if __name__ == "__main__":
    explain_loi()
    
    print("\n" + "=" * 60)
    print("\nInteractive Example:")
    print("-" * 60)
    try:
        n = int(input("Enter a number to see factorial with LOI: "))
        if n < 0:
            print("Please enter a non-negative number.")
        else:
            print(f"\nCalculating factorial({n}) with LOI:")
            print("-" * 60)
            result, max_level = factorial_with_loi(n)
            print(f"\nResult: {result}")
            print(f"Maximum Level of Indirection: {max_level}")
    except ValueError:
        print("Please enter a valid integer.")
