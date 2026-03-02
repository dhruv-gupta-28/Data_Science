"""
Recursion - Intermediate: Tree Node Definition

Basic tree node class for tree traversal examples.
"""

from typing import Optional


class TreeNode:
    """
    Binary tree node with left and right children.
    
    Attributes:
        value: The value stored in the node
        left: Reference to left child
        right: Reference to right child
    """
    
    def __init__(self, value: int) -> None:
        """
        Initialize a tree node.
        
        Args:
            value: The value to store in the node
        """
        self.value: int = value
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None


if __name__ == "__main__":
    # Create a sample tree
    #        1
    #       / \
    #      2   3
    #     / \
    #    4   5
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    print(f"Root value: {root.value}")
    print(f"Left child: {root.left.value}")
    print(f"Right child: {root.right.value}")
