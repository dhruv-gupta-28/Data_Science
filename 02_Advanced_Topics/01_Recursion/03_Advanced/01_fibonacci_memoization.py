"""
Recursion - Advanced: Fibonacci with Memoization

Optimize fibonacci using memoization to reduce time complexity.
"""

from typing import Dict


def fibonacci_memo(n: int, memo: Dict[int, int] | None = None) -> int:
    """
    Calculate nth fibonacci number using memoization.
    
    Time Complexity: O(n)
    Space Complexity: O(n) for memo dict
    
    Args:
        n: Position in fibonacci sequence (0-indexed)
        memo: Memoization dictionary to store results
        
    Returns:
        The nth fibonacci number
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


def fibonacci_tabulation(n: int) -> int:
    """
    Calculate nth fibonacci using bottom-up dynamic programming (tabulation).
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Args:
        n: Position in fibonacci sequence
        
    Returns:
        The nth fibonacci number
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    
    if n <= 1:
        return n
    
    dp: list[int] = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]


def fibonacci_optimized(n: int) -> int:
    """
    Calculate nth fibonacci with O(1) space complexity.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Args:
        n: Position in fibonacci sequence
        
    Returns:
        The nth fibonacci number
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    
    if n <= 1:
        return n
    
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    
    return curr


if __name__ == "__main__":
    test_n = 10
    
    print(f"Fibonacci({test_n}) using memoization: {fibonacci_memo(test_n)}")
    print(f"Fibonacci({test_n}) using tabulation: {fibonacci_tabulation(test_n)}")
    print(f"Fibonacci({test_n}) using optimized: {fibonacci_optimized(test_n)}")
    
    print("\nSequence comparison (n=0 to 15):")
    for i in range(16):
        memo_result = fibonacci_memo(i)
        tab_result = fibonacci_tabulation(i)
        opt_result = fibonacci_optimized(i)
        
        assert memo_result == tab_result == opt_result, f"Mismatch at {i}"
        print(f"  fib({i}) = {memo_result}")
