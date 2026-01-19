"""
Program 17: Find length of a string/list without using len()

Base case: If string/list is empty, return 0
Recursive case: Length = 1 + length of rest
"""

def length_string(s, index=0):
    """
    Find length of a string without using len() - index approach.
    
    Args:
        s (str): Input string
        index (int): Current index (used internally)
        
    Returns:
        int: Length of string
    """
    # Base case: reached end of string
    try:
        _ = s[index]
    except IndexError:
        return 0
    
    # Recursive case
    return 1 + length_string(s, index + 1)


def length_string_slicing(s):
    """
    Find length of a string without using len() - slicing approach.
    
    Args:
        s (str): Input string
        
    Returns:
        int: Length of string
    """
    # Base case
    if s == "":
        return 0
    
    # Recursive case
    return 1 + length_string_slicing(s[1:])


def length_list(arr, index=0):
    """
    Find length of a list without using len() - index approach.
    
    Args:
        arr (list): Input list
        index (int): Current index (used internally)
        
    Returns:
        int: Length of list
    """
    # Base case: reached end of list
    try:
        _ = arr[index]
    except IndexError:
        return 0
    
    # Recursive case
    return 1 + length_list(arr, index + 1)


def length_list_slicing(arr):
    """
    Find length of a list without using len() - slicing approach.
    
    Args:
        arr (list): Input list
        
    Returns:
        int: Length of list
    """
    # Base case
    if arr == []:
        return 0
    
    # Recursive case
    return 1 + length_list_slicing(arr[1:])


# Test cases
if __name__ == "__main__":
    print("Find Length without using len() - Recursion")
    print("-" * 40)
    
    test_strings = ["", "a", "hello", "python", "recursion"]
    test_lists = [[], [1], [1, 2, 3], [1, 2, 3, 4, 5], ['a', 'b', 'c']]
    
    print("\nString Length (index approach):")
    for s in test_strings:
        result = length_string(s)
        print(f"'{s}' -> Length: {result} (actual len: {len(s)})")
    
    print("\nString Length (slicing approach):")
    for s in test_strings:
        result = length_string_slicing(s)
        print(f"'{s}' -> Length: {result} (actual len: {len(s)})")
    
    print("\nList Length (index approach):")
    for arr in test_lists:
        result = length_list(arr)
        print(f"{arr} -> Length: {result} (actual len: {len(arr)})")
    
    print("\nList Length (slicing approach):")
    for arr in test_lists:
        result = length_list_slicing(arr)
        print(f"{arr} -> Length: {result} (actual len: {len(arr)})")
    
    # User input example
    user_input = input("\nEnter a string: ")
    result = length_string_slicing(user_input)
    print(f"Length of '{user_input}' is {result}")
