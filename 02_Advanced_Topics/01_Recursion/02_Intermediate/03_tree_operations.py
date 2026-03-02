"""
Recursion - Intermediate: Tree Height and Sum

Calculate tree properties using recursion.
"""

from typing import Optional


class TreeNode:
    """Binary tree node."""
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None


def tree_height(node: Optional[TreeNode]) -> int:
    """
    Calculate height of tree (max edges from root to leaf).
    
    Args:
        node: Root node
        
    Returns:
        Height of tree (-1 if empty)
    """
    if node is None:
        return -1
    
    left_height = tree_height(node.left)
    right_height = tree_height(node.right)
    
    return 1 + max(left_height, right_height)


def tree_sum(node: Optional[TreeNode]) -> int:
    """
    Calculate sum of all node values in tree.
    
    Args:
        node: Root node
        
    Returns:
        Sum of all node values
    """
    if node is None:
        return 0
    
    return node.value + tree_sum(node.left) + tree_sum(node.right)


def count_nodes(node: Optional[TreeNode]) -> int:
    """
    Count total number of nodes in tree.
    
    Args:
        node: Root node
        
    Returns:
        Number of nodes
    """
    if node is None:
        return 0
    
    return 1 + count_nodes(node.left) + count_nodes(node.right)


if __name__ == "__main__":
    # Create sample tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    print(f"Tree height: {tree_height(root)}")
    print(f"Tree sum: {tree_sum(root)}")
    print(f"Total nodes: {count_nodes(root)}")
