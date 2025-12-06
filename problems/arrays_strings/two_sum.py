"""
LeetCode 1. Two Sum
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two 
numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not 
use the same element twice.

Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]

Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Find two numbers that add up to target and return their indices.
    Uses a hash map for O(n) time complexity.
    """
    num_map = {}  # value -> index
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    
    return []  # No solution found


# Test cases
if __name__ == "__main__":
    # Test case 1
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    
    # Test case 2
    assert two_sum([3, 2, 4], 6) == [1, 2]
    
    # Test case 3
    assert two_sum([3, 3], 6) == [0, 1]
    
    print("All test cases passed!")
