"""
LeetCode 98. Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Example 1:
    Input: root = [2,1,3]
    Output: true

Example 2:
    Input: root = [5,1,4,null,null,3,6]
    Output: false
    Explanation: The root node's value is 5 but its right child's value is 4.

Time Complexity: O(n)
Space Complexity: O(h) where h is the height of the tree
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    """
    Validate BST using range checking.
    """
    def validate(node, min_val, max_val):
        if not node:
            return True
        
        if not (min_val < node.val < max_val):
            return False
        
        return (validate(node.left, min_val, node.val) and
                validate(node.right, node.val, max_val))
    
    return validate(root, float('-inf'), float('inf'))


def is_valid_bst_inorder(root: Optional[TreeNode]) -> bool:
    """
    Validate BST using in-order traversal.
    In-order traversal of BST should give sorted values.
    """
    prev = float('-inf')
    
    def inorder(node):
        nonlocal prev
        
        if not node:
            return True
        
        # Check left subtree
        if not inorder(node.left):
            return False
        
        # Check current node
        if node.val <= prev:
            return False
        prev = node.val
        
        # Check right subtree
        return inorder(node.right)
    
    return inorder(root)


# Test cases
if __name__ == "__main__":
    # Test case 1: [2,1,3] - valid BST
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    assert is_valid_bst(root) == True
    assert is_valid_bst_inorder(root) == True
    
    # Test case 2: [5,1,4,null,null,3,6] - invalid BST
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4, TreeNode(3), TreeNode(6))
    assert is_valid_bst(root) == False
    assert is_valid_bst_inorder(root) == False
    
    # Test case 3: empty tree
    assert is_valid_bst(None) == True
    
    # Test case 4: [5,4,6,null,null,3,7] - invalid (3 in wrong subtree)
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(6, TreeNode(3), TreeNode(7))
    assert is_valid_bst(root) == False
    
    print("All test cases passed!")
