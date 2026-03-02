"""
Recursion - Advanced: Coin Change Problem

Find minimum number of coins needed to make a given amount.
"""

from typing import List


def min_coins(coins: List[int], amount: int) -> int:
    """
    Find minimum number of coins to make given amount.
    
    Uses dynamic programming (bottom-up).
    
    Time Complexity: O(amount * len(coins))
    Space Complexity: O(amount)
    
    Args:
        coins: List of coin denominations
        amount: Target amount
        
    Returns:
        Minimum coins needed, or -1 if amount cannot be made
        
    Raises:
        ValueError: If amount is negative or coins list is empty
    """
    if amount < 0:
        raise ValueError("amount must be non-negative")
    
    if not coins:
        raise ValueError("coins list cannot be empty")
    
    if amount == 0:
        return 0
    
    # dp[i] = minimum coins needed to make amount i
    dp: list[int] = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for current_amount in range(1, amount + 1):
        for coin in coins:
            if coin <= current_amount:
                dp[current_amount] = min(dp[current_amount], dp[current_amount - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1


def min_coins_recursive(coins: List[int], amount: int, memo: dict[int, int] | None = None) -> int:
    """
    Recursive approach with memoization.
    
    Time Complexity: O(amount * len(coins))
    Space Complexity: O(amount)
    
    Args:
        coins: List of coin denominations
        amount: Target amount
        memo: Memoization dictionary
        
    Returns:
        Minimum coins needed, or -1 if impossible
        
    Raises:
        ValueError: If amount is negative or coins empty
    """
    if amount < 0:
        raise ValueError("amount must be non-negative")
    
    if not coins:
        raise ValueError("coins list cannot be empty")
    
    if memo is None:
        memo = {}
    
    if amount == 0:
        return 0
    
    if amount in memo:
        return memo[amount]
    
    min_needed = float('inf')
    for coin in coins:
        if coin <= amount:
            result = min_coins_recursive(coins, amount - coin, memo)
            if result >= 0:
                min_needed = min(min_needed, result + 1)
    
    memo[amount] = min_needed if min_needed != float('inf') else -1
    return memo[amount]


def get_coin_combination(coins: List[int], amount: int) -> List[int]:
    """
    Get the actual coins used to make minimum change.
    
    Args:
        coins: List of coin denominations
        amount: Target amount
        
    Returns:
        List of coins used, or empty list if impossible
    """
    dp: list[int] = [float('inf')] * (amount + 1)
    dp[0] = 0
    parent: list[int | None] = [None] * (amount + 1)
    
    for current_amount in range(1, amount + 1):
        for coin in coins:
            if coin <= current_amount and dp[current_amount - coin] + 1 < dp[current_amount]:
                dp[current_amount] = dp[current_amount - coin] + 1
                parent[current_amount] = coin
    
    # Reconstruct solution
    result: List[int] = []
    current = amount
    while current > 0 and parent[current] is not None:
        coin = parent[current]
        result.append(coin)
        current -= coin
    
    return result if dp[amount] != float('inf') else []


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 5], 5),
        ([2], 3),
        ([10], 1),
        ([1, 3, 4], 6),
        ([2, 5, 10], 27)
    ]
    
    for coins, amount in test_cases:
        min_needed = min_coins(coins, amount)
        recursive_result = min_coins_recursive(coins, amount)
        combination = get_coin_combination(coins, amount)
        
        print(f"Coins: {coins}, Amount: {amount}")
        print(f"  Minimum coins (iterative): {min_needed}")
        print(f"  Minimum coins (recursive): {recursive_result}")
        print(f"  Combination: {combination}")
        print()
