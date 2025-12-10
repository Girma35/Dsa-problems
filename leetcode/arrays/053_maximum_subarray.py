"""
LeetCode Problem 53: Maximum Subarray
Difficulty: Medium
Link: https://leetcode.com/problems/maximum-subarray/

Problem:
Given an integer array nums, find the subarray with the largest sum, and return its sum.

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

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Approach: Kadane's Algorithm
        Keep track of current sum and maximum sum.
        If current sum becomes negative, reset it to 0.
        """
        max_sum = nums[0]
        current_sum = 0
        
        for num in nums:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        
        return max_sum


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    assert solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    
    # Test case 2
    assert solution.maxSubArray([1]) == 1
    
    # Test case 3
    assert solution.maxSubArray([5, 4, -1, 7, 8]) == 23
    
    # Test case 4: All negative
    assert solution.maxSubArray([-1, -2, -3]) == -1
    
    print("All test cases passed!")
