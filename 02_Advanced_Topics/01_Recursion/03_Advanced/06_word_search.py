"""
Recursion - Advanced: Word Search in 2D Grid

Find if a word exists in a 2D grid with backtracking.
"""

from typing import List


def word_search(board: List[List[str]], word: str) -> bool:
    """
    Search for word in 2D grid (word can occur in 4 directions).
    
    Time Complexity: O(m * n * 4^l) where l is word length
    Space Complexity: O(l) for recursion stack
    
    Args:
        board: 2D grid of characters
        word: Word to search for
        
    Returns:
        True if word found, False otherwise
        
    Raises:
        ValueError: If board is empty or word is empty
    """
    if not board or not word:
        raise ValueError("board and word cannot be empty")
    
    m, n = len(board), len(board[0])
    visited: list[list[bool]] = [[False] * n for _ in range(m)]
    
    def dfs(i: int, j: int, idx: int) -> bool:
        """
        Depth-first search with backtracking.
        
        Args:
            i: Row index
            j: Column index
            idx: Current index in word
            
        Returns:
            True if word found from this position
        """
        if idx == len(word):
            return True
        
        if i < 0 or i >= m or j < 0 or j >= n or visited[i][j]:
            return False
        
        if board[i][j] != word[idx]:
            return False
        
        # Mark as visited
        visited[i][j] = True
        
        # Try 4 directions: up, down, left, right
        found = (
            dfs(i - 1, j, idx + 1) or
            dfs(i + 1, j, idx + 1) or
            dfs(i, j - 1, idx + 1) or
            dfs(i, j + 1, idx + 1)
        )
        
        # Backtrack
        visited[i][j] = False
        
        return found
    
    # Start search from each cell
    for i in range(m):
        for j in range(n):
            if dfs(i, j, 0):
                return True
    
    return False


def find_word_path(board: List[List[str]], word: str) -> List[tuple[int, int]] | None:
    """
    Find the path of the word in the grid.
    
    Args:
        board: 2D grid of characters
        word: Word to search for
        
    Returns:
        List of (row, col) coordinates, or None if not found
    """
    if not board or not word:
        raise ValueError("board and word cannot be empty")
    
    m, n = len(board), len(board[0])
    visited: list[list[bool]] = [[False] * n for _ in range(m)]
    path: List[tuple[int, int]] = []
    
    def dfs(i: int, j: int, idx: int) -> bool:
        if idx == len(word):
            return True
        
        if i < 0 or i >= m or j < 0 or j >= n or visited[i][j]:
            return False
        
        if board[i][j] != word[idx]:
            return False
        
        visited[i][j] = True
        path.append((i, j))
        
        found = (
            dfs(i - 1, j, idx + 1) or
            dfs(i + 1, j, idx + 1) or
            dfs(i, j - 1, idx + 1) or
            dfs(i, j + 1, idx + 1)
        )
        
        if not found:
            path.pop()
        
        visited[i][j] = False
        return found
    
    for i in range(m):
        for j in range(n):
            path.clear()
            if dfs(i, j, 0):
                return path[:]
    
    return None


def find_all_words(board: List[List[str]], words: List[str]) -> dict[str, bool]:
    """
    Find which words exist in the grid.
    
    Args:
        board: 2D grid of characters
        words: List of words to search
        
    Returns:
        Dictionary mapping word to whether it exists
    """
    result = {}
    for word in words:
        result[word] = word_search(board, word)
    return result


if __name__ == "__main__":
    # Test case 1
    board1 = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    
    test_words1 = ["ABCCED", "SEE", "ABCB", "ABFSAB"]
    
    print("Board 1:")
    for row in board1:
        print("  " + " ".join(row))
    
    for word in test_words1:
        exists = word_search(board1, word)
        path = find_word_path(board1, word)
        print(f"  Word '{word}': {exists}, Path: {path}")
    
    print()
    
    # Test case 2
    board2 = [
        ['D', 'P', 'O', 'G'],
        ['R', 'L', 'M', 'A'],
        ['A', 'C', 'Z', 'T']
    ]
    
    test_words2 = ["DPRLA", "GOAL", "DPR"]
    
    print("Board 2:")
    for row in board2:
        print("  " + " ".join(row))
    
    result = find_all_words(board2, test_words2)
    for word, found in result.items():
        print(f"  Word '{word}': {found}")
