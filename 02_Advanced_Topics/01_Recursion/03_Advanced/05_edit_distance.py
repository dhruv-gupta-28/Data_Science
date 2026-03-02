"""
Recursion - Advanced: Edit Distance

Find minimum edits (insert, delete, replace) to transform one string to another.
"""


def edit_distance(word1: str, word2: str) -> int:
    """
    Find minimum number of operations to transform word1 to word2.
    
    Operations: insert, delete, replace (each costs 1)
    
    Time Complexity: O(m * n)
    Space Complexity: O(m * n)
    
    Args:
        word1: Source string
        word2: Target string
        
    Returns:
        Minimum number of edits needed
    """
    m, n = len(word1), len(word2)
    
    # dp[i][j] = min edits to transform word1[:i] to word2[:j]
    dp: list[list[int]] = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Base cases
    for i in range(m + 1):
        dp[i][0] = i  # Delete all characters
    for j in range(n + 1):
        dp[0][j] = j  # Insert all characters
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                # Characters match
                dp[i][j] = dp[i-1][j-1]
            else:
                # Take minimum of three operations
                dp[i][j] = 1 + min(
                    dp[i-1][j],      # Delete
                    dp[i][j-1],      # Insert
                    dp[i-1][j-1]     # Replace
                )
    
    return dp[m][n]


def edit_distance_optimized(word1: str, word2: str) -> int:
    """
    Space-optimized version using only 1D array.
    
    Time Complexity: O(m * n)
    Space Complexity: O(n)
    
    Args:
        word1: Source string
        word2: Target string
        
    Returns:
        Minimum edits needed
    """
    m, n = len(word1), len(word2)
    
    prev: list[int] = list(range(n + 1))
    
    for i in range(1, m + 1):
        curr: list[int] = [i] + [0] * n
        
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                curr[j] = prev[j-1]
            else:
                curr[j] = 1 + min(prev[j], curr[j-1], prev[j-1])
        
        prev = curr
    
    return prev[n]


def get_edit_steps(word1: str, word2: str) -> list[str]:
    """
    Get the actual sequence of edits needed.
    
    Args:
        word1: Source string
        word2: Target string
        
    Returns:
        List of edit operations
    """
    m, n = len(word1), len(word2)
    
    dp: list[list[int]] = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    
    # Reconstruct path
    steps: list[str] = []
    i, j = m, n
    
    while i > 0 or j > 0:
        if i == 0:
            steps.append(f"Insert '{word2[j-1]}'")
            j -= 1
        elif j == 0:
            steps.append(f"Delete '{word1[i-1]}'")
            i -= 1
        elif word1[i-1] == word2[j-1]:
            i -= 1
            j -= 1
        else:
            min_val = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
            
            if dp[i-1][j-1] == min_val:
                steps.append(f"Replace '{word1[i-1]}' with '{word2[j-1]}'")
                i -= 1
                j -= 1
            elif dp[i-1][j] == min_val:
                steps.append(f"Delete '{word1[i-1]}'")
                i -= 1
            else:
                steps.append(f"Insert '{word2[j-1]}'")
                j -= 1
    
    return list(reversed(steps))


if __name__ == "__main__":
    test_cases = [
        ("horse", "ros"),
        ("intention", "execution"),
        ("a", "b"),
        ("abc", "abc"),
        ("", "abc")
    ]
    
    for word1, word2 in test_cases:
        distance = edit_distance(word1, word2)
        optimized = edit_distance_optimized(word1, word2)
        steps = get_edit_steps(word1, word2)
        
        print(f"From '{word1}' to '{word2}'")
        print(f"  Edit Distance (2D): {distance}")
        print(f"  Edit Distance (1D): {optimized}")
        print(f"  Steps:")
        for step in steps:
            print(f"    - {step}")
        print()
