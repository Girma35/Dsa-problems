"""
LeetCode 100. Same Tree
https://leetcode.com/problems/same-tree/

Given the roots of two binary trees p and q, write a function to check if they 
are the same or not.

Two binary trees are considered the same if they are structurally identical, 
and the nodes have the same value.

Example 1:
    Input: p = [1,2,3], q = [1,2,3]
    Output: true

Example 2:
    Input: p = [1,2], q = [1,null,2]
    Output: false

Example 3:
    Input: p = [1,2,1], q = [1,1,2]
    Output: false

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


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """
    Check if two binary trees are identical using recursion.
    """
    # Both empty
    if not p and not q:
        return True
    
    # One empty, one not
    if not p or not q:
        return False
    
    # Check value and recursively check children
    return (p.val == q.val and 
            is_same_tree(p.left, q.left) and 
            is_same_tree(p.right, q.right))


def is_same_tree_iterative(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """
    Check if two binary trees are identical using iteration.
    """
    queue = deque([(p, q)])
    
    while queue:
        node1, node2 = queue.popleft()
        
        if not node1 and not node2:
            continue
        
        if not node1 or not node2:
            return False
        
        if node1.val != node2.val:
            return False
        
        queue.append((node1.left, node2.left))
        queue.append((node1.right, node2.right))
    
    return True


# Test cases
if __name__ == "__main__":
    # Test case 1: p = [1,2,3], q = [1,2,3]
    p = TreeNode(1, TreeNode(2), TreeNode(3))
    q = TreeNode(1, TreeNode(2), TreeNode(3))
    assert is_same_tree(p, q) == True
    assert is_same_tree_iterative(p, q) == True
    
    # Test case 2: p = [1,2], q = [1,null,2]
    p = TreeNode(1, TreeNode(2))
    q = TreeNode(1, None, TreeNode(2))
    assert is_same_tree(p, q) == False
    assert is_same_tree_iterative(p, q) == False
    
    # Test case 3: p = [1,2,1], q = [1,1,2]
    p = TreeNode(1, TreeNode(2), TreeNode(1))
    q = TreeNode(1, TreeNode(1), TreeNode(2))
    assert is_same_tree(p, q) == False
    assert is_same_tree_iterative(p, q) == False
    
    # Test case 4: both empty
    assert is_same_tree(None, None) == True
    
    print("All test cases passed!")
