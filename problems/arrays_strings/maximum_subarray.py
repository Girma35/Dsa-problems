"""
LeetCode 53. Maximum Subarray
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the subarray with the largest sum, and return 
its sum.

Example 1:
    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
    Input: nums = [1]
    Output: 1
    Explanation: The subarray [1] has the largest sum 1.

Example 3:
    Input: nums = [5,4,-1,7,8]
    Output: 23
    Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Time Complexity: O(n)
Space Complexity: O(1)

Algorithm: Kadane's Algorithm
"""

from typing import List


def max_subarray(nums: List[int]) -> int:
    """
    Find maximum subarray sum using Kadane's Algorithm.
    """
    if not nums:
        return 0
    
    max_sum = nums[0]
    current_sum = nums[0]
    
    for i in range(1, len(nums)):
        # Either extend the previous subarray or start a new one
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum


# Test cases
if __name__ == "__main__":
    # Test case 1
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    
    # Test case 2
    assert max_subarray([1]) == 1
    
    # Test case 3
    assert max_subarray([5, 4, -1, 7, 8]) == 23
    
    # Test case 4 - all negative
    assert max_subarray([-3, -2, -1]) == -1
    
    print("All test cases passed!")
