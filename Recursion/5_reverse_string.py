"""
Program 5: Reverse a string using recursion

Base case: If string is empty or has one character, return it
Recursive case: Reverse the substring and append first character at the end
"""

def reverse_string(s):
    """
    Reverse a string using recursion.
    
    Args:
        s (str): Input string
        
    Returns:
        str: Reversed string
    """
    # Base case
    if len(s) <= 1:
        return s
    # Recursive case: reverse the rest and append first character
    return reverse_string(s[1:]) + s[0]


def reverse_string_index(s, start=0, end=None):
    """
    Reverse a string using recursion with indices.
    
    Args:
        s (str): Input string
        start (int): Starting index
        end (int): Ending index
        
    Returns:
        str: Reversed string
    """
    if end is None:
        end = len(s) - 1
    
    # Base case
    if start >= end:
        return s
    
    # Convert to list for swapping (strings are immutable)
    s_list = list(s)
    # Swap characters
    s_list[start], s_list[end] = s_list[end], s_list[start]
    # Recursive case
    return ''.join(reverse_string_index(''.join(s_list), start + 1, end - 1))


# Test cases
if __name__ == "__main__":
    print("Reverse String using Recursion")
    print("-" * 40)
    
    test_strings = ["hello", "python", "recursion", "a", "", "12345"]
    
    for s in test_strings:
        reversed_str = reverse_string(s)
        print(f"Original: '{s}' -> Reversed: '{reversed_str}'")
    
    # User input example
    user_input = input("\nEnter a string to reverse: ")
    reversed_input = reverse_string(user_input)
    print(f"Reversed string: '{reversed_input}'")
