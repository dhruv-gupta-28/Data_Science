"""
Program 12: Perform binary search using recursion

Binary search requires a sorted array.
Base case: If start > end, element not found
Recursive case: Compare target with middle element and search in appropriate half
"""

def binary_search(arr, target, start=0, end=None):
    """
    Perform binary search using recursion.
    
    Args:
        arr (list): Sorted list of elements
        target: Element to search for
        start (int): Starting index
        end (int): Ending index
        
    Returns:
        int: Index of target if found, -1 otherwise
    """
    if end is None:
        end = len(arr) - 1
    
    # Base case: element not found
    if start > end:
        return -1
    
    # Calculate middle index
    mid = (start + end) // 2
    
    # Base case: element found
    if arr[mid] == target:
        return mid
    
    # Recursive case: search in left or right half
    if arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, end)


# Test cases
if __name__ == "__main__":
    print("Binary Search using Recursion")
    print("-" * 40)
    
    # Test with sorted arrays
    test_arrays = [
        ([1, 2, 3, 4, 5], 3),
        ([1, 2, 3, 4, 5], 1),
        ([1, 2, 3, 4, 5], 5),
        ([1, 2, 3, 4, 5], 6),
        ([10, 20, 30, 40, 50, 60], 40),
        ([1, 3, 5, 7, 9, 11, 13, 15], 7),
        ([1, 3, 5, 7, 9, 11, 13, 15], 8),
        ([5], 5),
        ([5], 3),
    ]
    
    for arr, target in test_arrays:
        result = binary_search(arr, target)
        if result != -1:
            print(f"Target {target} found at index {result} in {arr}")
        else:
            print(f"Target {target} not found in {arr}")
    
    # User input example
    try:
        user_input = input("\nEnter sorted numbers separated by space: ")
        arr = sorted([int(x) for x in user_input.split()])
        target = int(input("Enter target to search: "))
        result = binary_search(arr, target)
        if result != -1:
            print(f"Target {target} found at index {result}")
        else:
            print(f"Target {target} not found in the array")
    except ValueError:
        print("Please enter valid integers.")
