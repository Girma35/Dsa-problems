"""
LeetCode 104. Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from 
the root node down to the farthest leaf node.

Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: 3

Example 2:
    Input: root = [1,null,2]
    Output: 2

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


def max_depth_recursive(root: Optional[TreeNode]) -> int:
    """
    Find maximum depth using DFS recursion.
    """
    if not root:
        return 0
    
    left_depth = max_depth_recursive(root.left)
    right_depth = max_depth_recursive(root.right)
    
    return max(left_depth, right_depth) + 1


def max_depth_iterative(root: Optional[TreeNode]) -> int:
    """
    Find maximum depth using BFS iteration.
    """
    if not root:
        return 0
    
    queue = deque([root])
    depth = 0
    
    while queue:
        depth += 1
        level_size = len(queue)
        
        for _ in range(level_size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return depth


# Test cases
if __name__ == "__main__":
    # Test case 1: [3,9,20,null,null,15,7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    assert max_depth_recursive(root) == 3
    assert max_depth_iterative(root) == 3
    
    # Test case 2: [1,null,2]
    root = TreeNode(1)
    root.right = TreeNode(2)
    assert max_depth_recursive(root) == 2
    assert max_depth_iterative(root) == 2
    
    # Test case 3: empty tree
    assert max_depth_recursive(None) == 0
    assert max_depth_iterative(None) == 0
    
    # Test case 4: single node
    root = TreeNode(1)
    assert max_depth_recursive(root) == 1
    assert max_depth_iterative(root) == 1
    
    print("All test cases passed!")
