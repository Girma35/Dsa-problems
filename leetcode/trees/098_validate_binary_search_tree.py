"""
LeetCode Problem 98: Validate Binary Search Tree
Difficulty: Medium
Link: https://leetcode.com/problems/validate-binary-search-tree/

Problem:
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

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -2^31 <= Node.val <= 2^31 - 1
"""

from typing import Optional
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Time Complexity: O(n)
        Space Complexity: O(h) where h is height of tree
        
        Approach: DFS with valid range for each node.
        """
        def validate(node, min_val, max_val):
            if not node:
                return True
            
            if node.val <= min_val or node.val >= max_val:
                return False
            
            return (validate(node.left, min_val, node.val) and 
                    validate(node.right, node.val, max_val))
        
        return validate(root, -math.inf, math.inf)
    
    def isValidBST_inorder(self, root: Optional[TreeNode]) -> bool:
        """
        Inorder traversal approach.
        A valid BST's inorder traversal produces sorted values.
        """
        prev = -math.inf
        stack = []
        current = root
        
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            
            if current.val <= prev:
                return False
            prev = current.val
            
            current = current.right
        
        return True


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: [2,1,3]
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    assert solution.isValidBST(root) == True
    
    # Test case 2: [5,1,4,null,null,3,6]
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)
    assert solution.isValidBST(root) == False
    
    # Test case 3: Single node
    assert solution.isValidBST(TreeNode(1)) == True
    
    # Test case 4: [5,4,6,null,null,3,7] - invalid because 3 < 5
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(6)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(7)
    assert solution.isValidBST(root) == False
    
    print("All test cases passed!")
