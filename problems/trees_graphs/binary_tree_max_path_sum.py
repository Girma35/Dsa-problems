"""
LeetCode 124. Binary Tree Maximum Path Sum
https://leetcode.com/problems/binary-tree-maximum-path-sum/

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes 
in the sequence has an edge connecting them. A node can only appear in the 
sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

Example 1:
    Input: root = [1,2,3]
    Output: 6
    Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:
    Input: root = [-10,9,20,null,null,15,7]
    Output: 42
    Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

Time Complexity: O(n)
Space Complexity: O(h) where h is the height of the tree
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_path_sum(root: Optional[TreeNode]) -> int:
    """
    Find maximum path sum using DFS.
    At each node, we consider:
    1. Path through this node (left + node + right)
    2. Best path from subtrees
    """
    max_sum = float('-inf')
    
    def dfs(node):
        nonlocal max_sum
        
        if not node:
            return 0
        
        # Get max contribution from left and right subtrees
        # If negative, we don't include it (use 0 instead)
        left_max = max(dfs(node.left), 0)
        right_max = max(dfs(node.right), 0)
        
        # Path sum through current node
        path_sum = left_max + node.val + right_max
        
        # Update global maximum
        max_sum = max(max_sum, path_sum)
        
        # Return max contribution to parent (can only go one direction)
        return node.val + max(left_max, right_max)
    
    dfs(root)
    return max_sum


# Test cases
if __name__ == "__main__":
    # Test case 1: [1,2,3]
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert max_path_sum(root) == 6
    
    # Test case 2: [-10,9,20,null,null,15,7]
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))
    assert max_path_sum(root) == 42
    
    # Test case 3: single negative node
    root = TreeNode(-3)
    assert max_path_sum(root) == -3
    
    # Test case 4: all negative
    root = TreeNode(-1, TreeNode(-2), TreeNode(-3))
    assert max_path_sum(root) == -1
    
    print("All test cases passed!")
