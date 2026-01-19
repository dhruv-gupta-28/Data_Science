"""
Program 16: Print numbers from N to 1 using recursion

This is the reverse of printing 1 to N.
Base case: If n < 1, return
Recursive case: Print n first, then recursively print n-1 to 1
"""

def print_n_to_1(n):
    """
    Print numbers from n to 1 using recursion.
    
    Args:
        n (int): Starting number (positive integer)
    """
    # Base case
    if n < 1:
        return
    
    # Print current number first
    print(n, end=" ")
    
    # Recursive case: print numbers from n-1 to 1
    print_n_to_1(n - 1)


def print_n_to_1_with_list(n, result=None):
    """
    Return list of numbers from n to 1 using recursion.
    
    Args:
        n (int): Starting number
        result (list): Accumulator list (used internally)
        
    Returns:
        list: List of numbers from n to 1
    """
    if result is None:
        result = []
    
    # Base case
    if n < 1:
        return result
    
    # Append current number first
    result.append(n)
    
    # Recursive case: build list from n-1 to 1
    print_n_to_1_with_list(n - 1, result)
    return result


# Test cases
if __name__ == "__main__":
    print("Print Numbers from N to 1 using Recursion")
    print("-" * 40)
    
    print("\nPrinting 10 to 1:")
    print_n_to_1(10)
    print()
    
    print("\nPrinting 5 to 1:")
    print_n_to_1(5)
    print()
    
    # Using list version
    print("\nNumbers from 15 to 1 (as list):")
    numbers = print_n_to_1_with_list(15)
    print(numbers)
    
    # User input example
    try:
        n = int(input("\nEnter a number N: "))
        if n < 1:
            print("Please enter a positive number.")
        else:
            print(f"\nNumbers from {n} to 1:")
            print_n_to_1(n)
            print()
    except ValueError:
        print("Please enter a valid integer.")
