"""
Recursion - Advanced: Longest Common Subsequence

Find longest common subsequence of two strings.
"""


def lcs_length(text1: str, text2: str) -> int:
    """
    Find length of longest common subsequence.
    
    Time Complexity: O(m * n)
    Space Complexity: O(m * n)
    
    Args:
        text1: First string
        text2: Second string
        
    Returns:
        Length of LCS
    """
    m, n = len(text1), len(text2)
    
    # dp[i][j] = LCS length of text1[:i] and text2[:j]
    dp: list[list[int]] = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]


def lcs_string(text1: str, text2: str) -> str:
    """
    Find the longest common subsequence string.
    
    Time Complexity: O(m * n)
    Space Complexity: O(m * n)
    
    Args:
        text1: First string
        text2: Second string
        
    Returns:
        The LCS string
    """
    m, n = len(text1), len(text2)
    
    dp: list[list[int]] = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Reconstruct LCS
    lcs_chars: list[str] = []
    i, j = m, n
    
    while i > 0 and j > 0:
        if text1[i-1] == text2[j-1]:
            lcs_chars.append(text1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    return ''.join(reversed(lcs_chars))


def lcs_with_indices(text1: str, text2: str) -> tuple[int, str]:
    """
    Find LCS length and the actual subsequence.
    
    Args:
        text1: First string
        text2: Second string
        
    Returns:
        Tuple of (length, lcs_string)
    """
    length = lcs_length(text1, text2)
    lcs = lcs_string(text1, text2)
    return (length, lcs)


def all_lcs(text1: str, text2: str) -> list[str]:
    """
    Find all longest common subsequences.
    
    Time Complexity: O(m * n + lcs_count)
    Space Complexity: O(m * n)
    
    Args:
        text1: First string
        text2: Second string
        
    Returns:
        List of all LCS strings
    """
    m, n = len(text1), len(text2)
    
    dp: list[list[int]] = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    def reconstruct(i: int, j: int) -> list[str]:
        """Reconstruct all possible LCS."""
        if i == 0 or j == 0:
            return [""]
        
        if text1[i-1] == text2[j-1]:
            return [sub + text1[i-1] for sub in reconstruct(i-1, j-1)]
        
        if dp[i-1][j] > dp[i][j-1]:
            return reconstruct(i-1, j)
        elif dp[i][j-1] > dp[i-1][j]:
            return reconstruct(i, j-1)
        else:
            # Both paths possible
            set1 = set(reconstruct(i-1, j))
            set2 = set(reconstruct(i, j-1))
            return list(set1 | set2)
    
    lcs_list = reconstruct(m, n)
    return sorted(list(set(lcs_list)))


if __name__ == "__main__":
    test_cases = [
        ("abcde", "ace"),
        ("abc", "abc"),
        ("abc", "def"),
        ("AGGTAB", "GXTXAYB"),
        ("OXCPQRSVWF", "SHMTULQRYPY")
    ]
    
    for text1, text2 in test_cases:
        length = lcs_length(text1, text2)
        lcs = lcs_string(text1, text2)
        all_lcss = all_lcs(text1, text2)
        
        print(f"Text1: '{text1}', Text2: '{text2}'")
        print(f"  LCS Length: {length}")
        print(f"  LCS String: '{lcs}'")
        print(f"  All LCS: {all_lcss}")
        print()
