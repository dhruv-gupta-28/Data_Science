"""
Recursion - Advanced: Subset Sum Problem

Determine if there exists a subset with given sum.
"""

from typing import List


def subset_sum_exists(arr: List[int], target: int) -> bool:
    """
    Check if there's a subset with given sum using DP.
    
    Time Complexity: O(n * target)
    Space Complexity: O(n * target)
    
    Args:
        arr: Array of integers
        target: Target sum
        
    Returns:
        True if subset exists, False otherwise
        
    Raises:
        ValueError: If target is negative
    """
    if target < 0:
        raise ValueError("target must be non-negative")
    
    n = len(arr)
    
    # dp[i][j] = True if sum j can be made with first i elements
    dp: list[list[bool]] = [[False] * (target + 1) for _ in range(n + 1)]
    
    # Sum 0 is always possible (empty subset)
    for i in range(n + 1):
        dp[i][0] = True
    
    for i in range(1, n + 1):
        for j in range(target + 1):
            # Don't include current element
            dp[i][j] = dp[i-1][j]
            
            # Include current element if possible
            if arr[i-1] <= j:
                dp[i][j] = dp[i][j] or dp[i-1][j - arr[i-1]]
    
    return dp[n][target]


def subset_sum_optimized(arr: List[int], target: int) -> bool:
    """
    Space-optimized subset sum using 1D DP array.
    
    Time Complexity: O(n * target)
    Space Complexity: O(target)
    
    Args:
        arr: Array of integers
        target: Target sum
        
    Returns:
        True if subset exists, False otherwise
    """
    if target < 0:
        raise ValueError("target must be non-negative")
    
    # dp[i] = True if sum i can be made
    dp: list[bool] = [False] * (target + 1)
    dp[0] = True
    
    for num in arr:
        # Iterate backwards to avoid using same element twice
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]
    
    return dp[target]


def get_subset(arr: List[int], target: int) -> List[int] | None:
    """
    Return the actual subset that sums to target, if it exists.
    
    Args:
        arr: Array of integers
        target: Target sum
        
    Returns:
        List of elements summing to target, or None if impossible
    """
    n = len(arr)
    dp: list[list[bool]] = [[False] * (target + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = True
    
    for i in range(1, n + 1):
        for j in range(target + 1):
            dp[i][j] = dp[i-1][j]
            if arr[i-1] <= j:
                dp[i][j] = dp[i][j] or dp[i-1][j - arr[i-1]]
    
    if not dp[n][target]:
        return None
    
    # Reconstruct subset
    subset: List[int] = []
    i, j = n, target
    
    while i > 0 and j > 0:
        # If value comes from including current element
        if not dp[i-1][j] and dp[i][j]:
            subset.append(arr[i-1])
            j -= arr[i-1]
        i -= 1
    
    return subset


if __name__ == "__main__":
    test_cases = [
        ([3, 34, 4, 12, 5, 2], 9),
        ([3, 34, 4, 12, 5, 2], 30),
        ([1, 5, 11, 5], 11),
        ([1, 2, 3, 7], 6)
    ]
    
    for arr, target in test_cases:
        exists = subset_sum_exists(arr, target)
        optimized = subset_sum_optimized(arr, target)
        subset = get_subset(arr, target)
        
        print(f"Array: {arr}, Target: {target}")
        print(f"  Exists (2D DP): {exists}")
        print(f"  Exists (1D DP): {optimized}")
        print(f"  Subset: {subset}")
        print(f"  Sum: {sum(subset) if subset else 'N/A'}")
        print()
