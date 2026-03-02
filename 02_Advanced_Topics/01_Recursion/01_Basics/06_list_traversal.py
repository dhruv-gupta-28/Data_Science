"""
Recursion: List Traversal

Print list elements recursively with indexing.
"""

from typing import Any


def print_list(lst: list[Any], index: int = 0) -> None:
    """
    Print list elements recursively.
    
    Args:
        lst: The list to print
        index: Current index (starts at 0)
        
    Returns:
        None
    """
    if index == len(lst):
        return
    
    print(lst[index], end=" ")
    print_list(lst, index + 1)


if __name__ == "__main__":
    print("List traversal:")
    print_list([1, 2, 3, 4, 5])
    print("\n")
    print_list(['a', 'b', 'c', 'd'])
    print()
