"""
Recursion - Intermediate: Merge Sort

Divide and conquer sorting algorithm.
"""

from typing import TypeVar, List

T = TypeVar('T')


def merge_sort(arr: List[int]) -> List[int]:
    """
    Sort array using merge sort (divide and conquer).
    
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    
    Args:
        arr: List to sort
        
    Returns:
        Sorted list
    """
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Merge
    return merge(left, right)


def merge(left: List[int], right: List[int]) -> List[int]:
    """
    Merge two sorted lists into one sorted list.
    
    Args:
        left: First sorted list
        right: Second sorted list
        
    Returns:
        Merged sorted list
    """
    result: List[int] = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result


if __name__ == "__main__":
    test_arrays = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 8, 1, 9, 3],
        [1],
        [4, 2, 4, 1]
    ]
    
    for arr in test_arrays:
        sorted_arr = merge_sort(arr.copy())
        print(f"Original: {arr}")
        print(f"Sorted:   {sorted_arr}\n")
