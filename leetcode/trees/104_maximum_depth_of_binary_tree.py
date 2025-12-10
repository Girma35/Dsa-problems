"""
LeetCode Problem 104: Maximum Depth of Binary Tree
Difficulty: Easy
Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/

Problem:
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the 
root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(h) where h is height of tree
        
        Approach: Recursive DFS
        """
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
    def maxDepth_iterative(self, root: Optional[TreeNode]) -> int:
        """
        Iterative BFS approach.
        """
        if not root:
            return 0
        
        queue = deque([root])
        depth = 0
        
        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return depth


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: [3,9,20,null,null,15,7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    assert solution.maxDepth(root) == 3
    
    # Test case 2: [1,null,2]
    root = TreeNode(1)
    root.right = TreeNode(2)
    assert solution.maxDepth(root) == 2
    
    # Test case 3: Empty tree
    assert solution.maxDepth(None) == 0
    
    # Test case 4: Single node
    assert solution.maxDepth(TreeNode(1)) == 1
    
    print("All test cases passed!")
