"""
Program 9: Find sum of digits of a number using recursion

Base case: If number is less than 10, return the number itself
Recursive case: Sum of digits = last digit + sum of digits in remaining number
"""

def sum_of_digits(n):
    """
    Calculate sum of digits in a number using recursion.
    
    Args:
        n (int): Input number
        
    Returns:
        int: Sum of all digits
    """
    # Handle negative numbers
    n = abs(n)
    
    # Base case
    if n < 10:
        return n
    
    # Recursive case: last digit + sum of remaining digits
    return (n % 10) + sum_of_digits(n // 10)


# Test cases
if __name__ == "__main__":
    print("Sum of Digits using Recursion")
    print("-" * 40)
    
    test_cases = [0, 1, 9, 10, 123, 4567, 999, 1000, -123]
    
    for num in test_cases:
        digit_sum = sum_of_digits(num)
        print(f"Number: {num:>6} -> Sum of digits: {digit_sum}")
    
    # User input example
    try:
        n = int(input("\nEnter a number: "))
        digit_sum = sum_of_digits(n)
        print(f"Sum of digits in {n} is {digit_sum}")
    except ValueError:
        print("Please enter a valid integer.")
