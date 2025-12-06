"""
LeetCode Problem 100: Same Tree
Difficulty: Easy
Link: https://leetcode.com/problems/same-tree/

Problem:
Given the roots of two binary trees p and q, write a function to check if they are 
the same or not.

Two binary trees are considered the same if they are structurally identical, and 
the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false

Constraints:
- The number of nodes in both trees is in the range [0, 100].
- -10^4 <= Node.val <= 10^4
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Time Complexity: O(n)
        Space Complexity: O(h) where h is height of tree
        
        Approach: Recursive comparison of nodes.
        """
        # Both empty
        if not p and not q:
            return True
        
        # One empty, one not
        if not p or not q:
            return False
        
        # Different values
        if p.val != q.val:
            return False
        
        # Recursively check subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: [1,2,3] and [1,2,3]
    p = TreeNode(1, TreeNode(2), TreeNode(3))
    q = TreeNode(1, TreeNode(2), TreeNode(3))
    assert solution.isSameTree(p, q) == True
    
    # Test case 2: [1,2] and [1,null,2]
    p = TreeNode(1, TreeNode(2))
    q = TreeNode(1, None, TreeNode(2))
    assert solution.isSameTree(p, q) == False
    
    # Test case 3: [1,2,1] and [1,1,2]
    p = TreeNode(1, TreeNode(2), TreeNode(1))
    q = TreeNode(1, TreeNode(1), TreeNode(2))
    assert solution.isSameTree(p, q) == False
    
    # Test case 4: Both empty
    assert solution.isSameTree(None, None) == True
    
    print("All test cases passed!")
