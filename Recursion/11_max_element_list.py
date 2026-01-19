"""
Program 11: Find the maximum element in a list using recursion

Base case: If list has one element, return that element
Recursive case: Compare first element with maximum of rest of the list
"""

def max_element(arr, index=0):
    """
    Find maximum element in a list using recursion.
    
    Args:
        arr (list): Input list
        index (int): Current index (used internally)
        
    Returns:
        Maximum element in the list
    """
    # Base case: if only one element left
    if index == len(arr) - 1:
        return arr[index]
    
    # Recursive case: compare current element with max of rest
    current = arr[index]
    max_rest = max_element(arr, index + 1)
    return current if current > max_rest else max_rest


def max_element_slicing(arr):
    """
    Find maximum element using list slicing approach.
    
    Args:
        arr (list): Input list
        
    Returns:
        Maximum element in the list
    """
    # Base case
    if len(arr) == 1:
        return arr[0]
    
    # Recursive case: compare first element with max of rest
    return max(arr[0], max_element_slicing(arr[1:]))


# Test cases
if __name__ == "__main__":
    print("Find Maximum Element in List using Recursion")
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
        result = max_element(arr)
        print(f"List: {arr} -> Max: {result}")
    
    print("\nUsing slicing approach:")
    for arr in test_lists:
        result = max_element_slicing(arr)
        print(f"List: {arr} -> Max: {result}")
    
    # User input example
    try:
        user_input = input("\nEnter numbers separated by space: ")
        arr = [int(x) for x in user_input.split()]
        if arr:
            result = max_element(arr)
            print(f"Maximum element: {result}")
        else:
            print("List is empty.")
    except ValueError:
        print("Please enter valid integers.")
