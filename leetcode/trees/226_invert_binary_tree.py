"""
LeetCode Problem 226: Invert Binary Tree
Difficulty: Easy
Link: https://leetcode.com/problems/invert-binary-tree/

Problem:
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

Constraints:
- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100
"""

from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Time Complexity: O(n)
        Space Complexity: O(h) where h is height of tree
        
        Approach: Recursive DFS - swap left and right children at each node.
        """
        if not root:
            return None
        
        # Swap children
        root.left, root.right = root.right, root.left
        
        # Recursively invert subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
    
    def invertTree_iterative(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Iterative BFS approach.
        """
        if not root:
            return None
        
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return root


# Helper function to convert tree to list (level order)
def tree_to_list(root):
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
    solution = Solution()
    
    # Test case 1: [4,2,7,1,3,6,9]
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    result = solution.invertTree(root)
    assert tree_to_list(result) == [4, 7, 2, 9, 6, 3, 1]
    
    # Test case 2: [2,1,3]
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    result = solution.invertTree(root)
    assert tree_to_list(result) == [2, 3, 1]
    
    # Test case 3: Empty tree
    assert solution.invertTree(None) is None
    
    print("All test cases passed!")
