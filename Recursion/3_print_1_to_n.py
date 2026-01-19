"""
Program 3: Print numbers from 1 to N using recursion

This program demonstrates how to print numbers in ascending order
using recursion without using loops.
"""

def print_1_to_n(n):
    """
    Print numbers from 1 to n using recursion.
    
    Args:
        n (int): Upper limit (positive integer)
    """
    # Base case
    if n < 1:
        return
    # Recursive case: print numbers from 1 to n-1 first, then n
    print_1_to_n(n - 1)
    print(n, end=" ")


def print_1_to_n_with_list(n, result=None):
    """
    Return list of numbers from 1 to n using recursion.
    
    Args:
        n (int): Upper limit
        result (list): Accumulator list (used internally)
        
    Returns:
        list: List of numbers from 1 to n
    """
    if result is None:
        result = []
    
    # Base case
    if n < 1:
        return result
    
    # Recursive case: build list from 1 to n-1, then append n
    print_1_to_n_with_list(n - 1, result)
    result.append(n)
    return result


# Test cases
if __name__ == "__main__":
    print("Print Numbers from 1 to N using Recursion")
    print("-" * 40)
    
    print("\nPrinting 1 to 10:")
    print_1_to_n(10)
    print()
    
    print("\nPrinting 1 to 5:")
    print_1_to_n(5)
    print()
    
    # Using list version
    print("\nNumbers from 1 to 15 (as list):")
    numbers = print_1_to_n_with_list(15)
    print(numbers)
    
    # User input example
    try:
        n = int(input("\nEnter a number N: "))
        if n < 1:
            print("Please enter a positive number.")
        else:
            print(f"\nNumbers from 1 to {n}:")
            print_1_to_n(n)
            print()
    except ValueError:
        print("Please enter a valid integer.")
