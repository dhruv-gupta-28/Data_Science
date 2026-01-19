"""
Program 10: Check even or odd using indirect recursion

Indirect recursion: Function A calls function B, which calls function A.
This program uses two functions that call each other recursively.

Base case: n == 0 (even), n == 1 (odd)
Recursive case: 
    - is_even(n) calls is_odd(n-1)
    - is_odd(n) calls is_even(n-1)
"""

def is_even(n):
    """
    Check if a number is even using indirect recursion.
    
    Args:
        n (int): Input number (non-negative)
        
    Returns:
        bool: True if even, False if odd
    """
    # Base case
    if n == 0:
        return True
    
    # Indirect recursion: call is_odd
    return is_odd(n - 1)


def is_odd(n):
    """
    Check if a number is odd using indirect recursion.
    
    Args:
        n (int): Input number (non-negative)
        
    Returns:
        bool: True if odd, False if even
    """
    # Base case
    if n == 0:
        return False
    
    # Indirect recursion: call is_even
    return is_even(n - 1)


# Test cases
if __name__ == "__main__":
    print("Check Even or Odd using Indirect Recursion")
    print("-" * 40)
    
    test_cases = [0, 1, 2, 3, 4, 5, 10, 15, 20, 25]
    
    print("\nUsing is_even():")
    for num in test_cases:
        result = is_even(num)
        print(f"{num:>3} is {'Even' if result else 'Odd'}")
    
    print("\nUsing is_odd():")
    for num in test_cases:
        result = is_odd(num)
        print(f"{num:>3} is {'Odd' if result else 'Even'}")
    
    # User input example
    try:
        n = int(input("\nEnter a number: "))
        if n < 0:
            print("Please enter a non-negative number.")
        else:
            if is_even(n):
                print(f"{n} is Even")
            else:
                print(f"{n} is Odd")
    except ValueError:
        print("Please enter a valid integer.")
