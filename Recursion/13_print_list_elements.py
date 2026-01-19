"""
Program 13: Print all elements of a list using recursion

Base case: If list is empty, return
Recursive case: Print first element, then recursively print rest
"""

def print_list_elements(arr, index=0):
    """
    Print all elements of a list using recursion (index-based).
    
    Args:
        arr (list): Input list
        index (int): Current index (used internally)
    """
    # Base case
    if index >= len(arr):
        return
    
    # Print current element
    print(arr[index], end=" ")
    
    # Recursive case: print next element
    print_list_elements(arr, index + 1)


def print_list_elements_slicing(arr):
    """
    Print all elements using list slicing approach.
    
    Args:
        arr (list): Input list
    """
    # Base case
    if len(arr) == 0:
        return
    
    # Print first element
    print(arr[0], end=" ")
    
    # Recursive case: print rest of the list
    print_list_elements_slicing(arr[1:])


def get_list_elements(arr):
    """
    Return all elements as a list (for demonstration).
    
    Args:
        arr (list): Input list
        
    Returns:
        list: Same list (demonstrates traversal)
    """
    if len(arr) == 0:
        return []
    
    return [arr[0]] + get_list_elements(arr[1:])


# Test cases
if __name__ == "__main__":
    print("Print All Elements of a List using Recursion")
    print("-" * 40)
    
    test_lists = [
        [1, 2, 3, 4, 5],
        ['a', 'b', 'c', 'd'],
        [10, 20, 30],
        [42],
        []
    ]
    
    print("\nUsing index-based approach:")
    for arr in test_lists:
        print(f"List: {arr}")
        print("Elements: ", end="")
        print_list_elements(arr)
        print()
    
    print("\nUsing slicing approach:")
    for arr in test_lists:
        print(f"List: {arr}")
        print("Elements: ", end="")
        print_list_elements_slicing(arr)
        print()
    
    # User input example
    try:
        user_input = input("\nEnter elements separated by space: ")
        if user_input.strip():
            arr = user_input.split()
            print("Elements: ", end="")
            print_list_elements(arr)
            print()
        else:
            print("List is empty.")
    except Exception as e:
        print(f"Error: {e}")
