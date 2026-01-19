"""
Program 14: Find minimum element in a list using recursion

Base case: If list has one element, return that element
Recursive case: Compare first element with minimum of rest of the list
"""

def min_element(arr, index=0):
    """
    Find minimum element in a list using recursion.
    
    Args:
        arr (list): Input list
        index (int): Current index (used internally)
        
    Returns:
        Minimum element in the list
    """
    # Base case: if only one element left
    if index == len(arr) - 1:
        return arr[index]
    
    # Recursive case: compare current element with min of rest
    current = arr[index]
    min_rest = min_element(arr, index + 1)
    return current if current < min_rest else min_rest


def min_element_slicing(arr):
    """
    Find minimum element using list slicing approach.
    
    Args:
        arr (list): Input list
        
    Returns:
        Minimum element in the list
    """
    # Base case
    if len(arr) == 1:
        return arr[0]
    
    # Recursive case: compare first element with min of rest
    return min(arr[0], min_element_slicing(arr[1:]))


# Test cases
if __name__ == "__main__":
    print("Find Minimum Element in List using Recursion")
    print("-" * 40)
    
    test_lists = [
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [10, 20, 5, 30, 15],
        [42],
        [-5, -2, -10, -1],
        [1, 3, 2, 8, 4, 7, 6, 5]
    ]
    
    print("\nUsing index-based approach:")
    for arr in test_lists:
        result = min_element(arr)
        print(f"List: {arr} -> Min: {result}")
    
    print("\nUsing slicing approach:")
    for arr in test_lists:
        result = min_element_slicing(arr)
        print(f"List: {arr} -> Min: {result}")
    
    # User input example
    try:
        user_input = input("\nEnter numbers separated by space: ")
        arr = [int(x) for x in user_input.split()]
        if arr:
            result = min_element(arr)
            print(f"Minimum element: {result}")
        else:
            print("List is empty.")
    except ValueError:
        print("Please enter valid integers.")
