"""
LeetCode 226. Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/

Given the root of a binary tree, invert the tree, and return its root.

Example 1:
    Input: root = [4,2,7,1,3,6,9]
    Output: [4,7,2,9,6,3,1]

Example 2:
    Input: root = [2,1,3]
    Output: [2,3,1]

Example 3:
    Input: root = []
    Output: []

Time Complexity: O(n)
Space Complexity: O(h) where h is the height of the tree
"""

from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    Invert binary tree using recursion.
    """
    if not root:
        return None
    
    # Swap children
    root.left, root.right = root.right, root.left
    
    # Recursively invert subtrees
    invert_tree(root.left)
    invert_tree(root.right)
    
    return root


def invert_tree_iterative(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    Invert binary tree using BFS iteration.
    """
    if not root:
        return None
    
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        
        # Swap children
        node.left, node.right = node.right, node.left
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return root


# Helper function for testing
def tree_to_list(root):
    """Convert tree to level-order list for testing."""
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # Remove trailing Nones
    while result and result[-1] is None:
        result.pop()
    
    return result


# Test cases
if __name__ == "__main__":
    # Test case 1: [4,2,7,1,3,6,9] -> [4,7,2,9,6,3,1]
    root = TreeNode(4)
    root.left = TreeNode(2, TreeNode(1), TreeNode(3))
    root.right = TreeNode(7, TreeNode(6), TreeNode(9))
    inverted = invert_tree(root)
    assert tree_to_list(inverted) == [4, 7, 2, 9, 6, 3, 1]
    
    # Test case 2: [2,1,3] -> [2,3,1]
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    inverted = invert_tree(root)
    assert tree_to_list(inverted) == [2, 3, 1]
    
    # Test case 3: empty tree
    assert invert_tree(None) is None
    
    print("All test cases passed!")
