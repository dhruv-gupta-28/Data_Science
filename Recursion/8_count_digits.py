"""
Program 8: Count digits in a number using recursion

Base case: If number is less than 10, it has 1 digit
Recursive case: Count digits in n//10 and add 1
"""

def count_digits(n):
    """
    Count the number of digits in a number using recursion.
    
    Args:
        n (int): Input number
        
    Returns:
        int: Number of digits
    """
    # Handle negative numbers
    n = abs(n)
    
    # Base case
    if n < 10:
        return 1
    
    # Recursive case: count digits in n//10 and add 1
    return 1 + count_digits(n // 10)


# Test cases
if __name__ == "__main__":
    print("Count Digits in a Number using Recursion")
    print("-" * 40)
    
    test_cases = [0, 1, 9, 10, 99, 100, 1234, 98765, -123, -1]
    
    for num in test_cases:
        digit_count = count_digits(num)
        print(f"Number: {num:>8} -> Digits: {digit_count}")
    
    # User input example
    try:
        n = int(input("\nEnter a number: "))
        digit_count = count_digits(n)
        print(f"Number of digits in {n} is {digit_count}")
    except ValueError:
        print("Please enter a valid integer.")
