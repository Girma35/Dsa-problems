"""
LeetCode 46. Permutations
https://leetcode.com/problems/permutations/

Given an array nums of distinct integers, return all the possible permutations. 
You can return the answer in any order.

Example 1:
    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
    Input: nums = [0,1]
    Output: [[0,1],[1,0]]

Example 3:
    Input: nums = [1]
    Output: [[1]]

Time Complexity: O(n! * n)
Space Complexity: O(n) for recursion stack
"""

from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    """
    Generate all permutations using backtracking.
    """
    result = []
    
    def backtrack(current):
        if len(current) == len(nums):
            result.append(current[:])
            return
        
        for num in nums:
            if num not in current:
                current.append(num)
                backtrack(current)
                current.pop()
    
    backtrack([])
    return result


def permute_swap(nums: List[int]) -> List[List[int]]:
    """
    Generate permutations using swap method.
    """
    result = []
    
    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])
            return
        
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]
    
    backtrack(0)
    return result


# Test cases
if __name__ == "__main__":
    # Test case 1
    result = permute([1, 2, 3])
    expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    assert sorted(result) == sorted(expected)
    
    # Test case 2
    result = permute([0, 1])
    expected = [[0, 1], [1, 0]]
    assert sorted(result) == sorted(expected)
    
    # Test case 3
    assert permute([1]) == [[1]]
    
    # Test swap method
    result = permute_swap([1, 2])
    assert sorted(result) == [[1, 2], [2, 1]]
    
    print("All test cases passed!")
