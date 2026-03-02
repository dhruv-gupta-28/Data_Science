"""
Recursion - Intermediate: Tree Traversal Methods

Three ways to traverse a binary tree recursively.
"""

from typing import Optional


class TreeNode:
    """Binary tree node."""
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None


def preorder(node: Optional[TreeNode]) -> None:
    """
    Preorder traversal: Root, Left, Right.
    
    Args:
        node: Current node
    """
    if node is None:
        return
    
    print(node.value, end=" ")  # Process node
    preorder(node.left)          # Process left subtree
    preorder(node.right)         # Process right subtree


def inorder(node: Optional[TreeNode]) -> None:
    """
    Inorder traversal: Left, Root, Right.
    
    Args:
        node: Current node
    """
    if node is None:
        return
    
    inorder(node.left)           # Process left subtree
    print(node.value, end=" ")   # Process node
    inorder(node.right)          # Process right subtree


def postorder(node: Optional[TreeNode]) -> None:
    """
    Postorder traversal: Left, Right, Root.
    
    Args:
        node: Current node
    """
    if node is None:
        return
    
    postorder(node.left)         # Process left subtree
    postorder(node.right)        # Process right subtree
    print(node.value, end=" ")   # Process node


if __name__ == "__main__":
    # Create sample tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    print("Preorder traversal: ", end="")
    preorder(root)
    print("\n")
    
    print("Inorder traversal: ", end="")
    inorder(root)
    print("\n")
    
    print("Postorder traversal: ", end="")
    postorder(root)
    print()
