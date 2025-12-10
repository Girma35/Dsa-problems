"""
LeetCode 102. Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/

Given the root of a binary tree, return the level order traversal of its nodes' 
values. (i.e., from left to right, level by level).

Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[9,20],[15,7]]

Example 2:
    Input: root = [1]
    Output: [[1]]

Example 3:
    Input: root = []
    Output: []

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Level order traversal using BFS.
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result


def level_order_recursive(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Level order traversal using DFS recursion.
    """
    result = []
    
    def dfs(node, level):
        if not node:
            return
        
        # Create new level if needed
        if len(result) == level:
            result.append([])
        
        result[level].append(node.val)
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)
    
    dfs(root, 0)
    return result


# Test cases
if __name__ == "__main__":
    # Test case 1: [3,9,20,null,null,15,7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))
    assert level_order(root) == [[3], [9, 20], [15, 7]]
    assert level_order_recursive(root) == [[3], [9, 20], [15, 7]]
    
    # Test case 2: [1]
    root = TreeNode(1)
    assert level_order(root) == [[1]]
    
    # Test case 3: empty tree
    assert level_order(None) == []
    
    print("All test cases passed!")
