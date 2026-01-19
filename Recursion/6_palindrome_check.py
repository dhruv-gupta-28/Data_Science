"""
Program 6: Check whether a string is palindrome using recursion

A palindrome reads the same forwards and backwards.
Examples: "racecar", "level", "a", ""

Base case: If string has 0 or 1 character, it's a palindrome
Recursive case: Check if first and last characters match,
                and the substring between them is also a palindrome
"""

def is_palindrome(s):
    """
    Check if a string is palindrome using recursion.
    
    Args:
        s (str): Input string (case-insensitive)
        
    Returns:
        bool: True if palindrome, False otherwise
    """
    # Convert to lowercase and remove spaces for better checking
    s = s.lower().replace(" ", "")
    
    # Base case
    if len(s) <= 1:
        return True
    
    # Recursive case: check first and last characters
    if s[0] != s[-1]:
        return False
    
    # Check the substring between first and last
    return is_palindrome(s[1:-1])


def is_palindrome_index(s, start=0, end=None):
    """
    Check if a string is palindrome using recursion with indices.
    
    Args:
        s (str): Input string
        start (int): Starting index
        end (int): Ending index
        
    Returns:
        bool: True if palindrome, False otherwise
    """
    if end is None:
        end = len(s) - 1
    
    # Base case
    if start >= end:
        return True
    
    # Recursive case: check characters at start and end
    if s[start].lower() != s[end].lower():
        return False
    
    return is_palindrome_index(s, start + 1, end - 1)


# Test cases
if __name__ == "__main__":
    print("Palindrome Check using Recursion")
    print("-" * 40)
    
    test_strings = [
        "racecar",
        "level",
        "hello",
        "python",
        "a",
        "",
        "A man a plan a canal Panama",
        "Madam",
        "12321",
        "12345"
    ]
    
    for s in test_strings:
        result = is_palindrome(s)
        status = "✓ Palindrome" if result else "✗ Not Palindrome"
        print(f"'{s}' -> {status}")
    
    # User input example
    user_input = input("\nEnter a string to check: ")
    result = is_palindrome(user_input)
    if result:
        print(f"'{user_input}' is a palindrome!")
    else:
        print(f"'{user_input}' is not a palindrome.")
