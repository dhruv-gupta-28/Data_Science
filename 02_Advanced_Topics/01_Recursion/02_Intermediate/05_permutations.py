"""
Recursion - Intermediate: Permutations

Generate all permutations of a list using backtracking.
"""

from typing import List


def generate_permutations(arr: List[int]) -> List[List[int]]:
    """
    Generate all permutations of array using backtracking.
    
    Args:
        arr: List to permute
        
    Returns:
        List of all permutations
    """
    result: List[List[int]] = []
    
    def backtrack(current: List[int], remaining: List[int]) -> None:
        """
        Backtracking helper function.
        
        Args:
            current: Current permutation being built
            remaining: Remaining elements to add
        """
        if not remaining:
            result.append(current[:])
            return
        
        for i in range(len(remaining)):
            # Choose
            current.append(remaining[i])
            
            # Explore
            new_remaining = remaining[:i] + remaining[i+1:]
            backtrack(current, new_remaining)
            
            # Unchoose (backtrack)
            current.pop()
    
    backtrack([], arr)
    return result


if __name__ == "__main__":
    test_cases = [
        [1, 2, 3],
        [1, 2],
        ['a', 'b', 'c']
    ]
    
    for test in test_cases:
        perms = generate_permutations(test)
        print(f"Permutations of {test}:")
        for perm in perms:
            print(f"  {perm}")
        print()
