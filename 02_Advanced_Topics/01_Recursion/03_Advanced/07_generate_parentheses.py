"""
Recursion - Advanced: Generate Valid Parentheses

Generate all combinations of valid parentheses.
"""

from typing import List


def generate_parentheses(n: int) -> List[str]:
    """
    Generate all valid combinations of n pairs of parentheses.
    
    Time Complexity: O(4^n / sqrt(n)) - Catalan number
    Space Complexity: O(n) for recursion depth
    
    Args:
        n: Number of parenthesis pairs
        
    Returns:
        List of valid parenthesis combinations
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    
    result: List[str] = []
    
    def backtrack(current: str, open_count: int, close_count: int) -> None:
        """
        Build valid parentheses recursively.
        
        Args:
            current: Current string being built
            open_count: Number of open parentheses used
            close_count: Number of close parentheses used
        """
        # Base case: all parentheses placed
        if len(current) == 2 * n:
            result.append(current)
            return
        
        # Add open parenthesis if we haven't used all
        if open_count < n:
            backtrack(current + '(', open_count + 1, close_count)
        
        # Add close parenthesis if valid (close count < open count)
        if close_count < open_count:
            backtrack(current + ')', open_count, close_count + 1)
    
    backtrack('', 0, 0)
    return result


def is_valid_parentheses(s: str) -> bool:
    """
    Check if parentheses string is valid.
    
    Args:
        s: String to check
        
    Returns:
        True if valid, False otherwise
    """
    count = 0
    for char in s:
        if char == '(':
            count += 1
        else:
            count -= 1
        
        if count < 0:
            return False
    
    return count == 0


def count_valid_parentheses(n: int) -> int:
    """
    Count number of valid parenthesis combinations (Catalan number).
    
    C(n) = (2n)! / ((n+1)! * n!)
    
    Args:
        n: Number of pairs
        
    Returns:
        Count of valid combinations
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    
    if n <= 1:
        return 1
    
    # Using DP to calculate nth Catalan number
    dp: list[int] = [0] * (n + 1)
    dp[0] = dp[1] = 1
    
    for i in range(2, n + 1):
        for j in range(i):
            dp[i] += dp[j] * dp[i - 1 - j]
    
    return dp[n]


def generate_with_balanced_constraint(n: int) -> List[str]:
    """
    Generate valid parentheses ensuring balanced pairs at each step.
    
    Args:
        n: Number of pairs
        
    Returns:
        List of valid combinations
    """
    def backtrack(current: str, open_count: int, close_count: int) -> None:
        if open_count == n and close_count == n:
            result.append(current)
            return
        
        # Add open parenthesis
        if open_count < n:
            backtrack(current + '(', open_count + 1, close_count)
        
        # Add close parenthesis only if beneficial
        if close_count < open_count:
            backtrack(current + ')', open_count, close_count + 1)
    
    result: List[str] = []
    backtrack('', 0, 0)
    return result


if __name__ == "__main__":
    test_cases = [0, 1, 2, 3, 4]
    
    for n in test_cases:
        combinations = generate_parentheses(n)
        count = count_valid_parentheses(n)
        
        print(f"n = {n}:")
        print(f"  Count: {count}")
        print(f"  Combinations: {combinations}")
        
        # Verify all are valid
        all_valid = all(is_valid_parentheses(combo) for combo in combinations)
        print(f"  All valid: {all_valid}")
        print()
    
    # Catalan number sequence
    print("Catalan numbers (first 10):")
    catalan = [count_valid_parentheses(i) for i in range(10)]
    print(f"  {catalan}")
