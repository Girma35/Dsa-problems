"""
LeetCode Problem 300: Longest Increasing Subsequence
Difficulty: Medium
Link: https://leetcode.com/problems/longest-increasing-subsequence/

Problem:
Given an integer array nums, return the length of the longest strictly increasing 
subsequence.

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1

Constraints:
- 1 <= nums.length <= 2500
- -10^4 <= nums[i] <= 10^4
"""

from typing import List
import bisect


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        
        Approach: Dynamic Programming
        dp[i] = length of LIS ending at index i
        """
        if not nums:
            return 0
        
        n = len(nums)
        dp = [1] * n
        
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
    
    def lengthOfLIS_binary_search(self, nums: List[int]) -> int:
        """
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        
        Approach: Binary search with auxiliary array.
        """
        if not nums:
            return 0
        
        tails = []
        
        for num in nums:
            pos = bisect.bisect_left(tails, num)
            if pos == len(tails):
                tails.append(num)
            else:
                tails[pos] = num
        
        return len(tails)


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    assert solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    
    # Test case 2
    assert solution.lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4
    
    # Test case 3
    assert solution.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]) == 1
    
    # Test binary search approach
    assert solution.lengthOfLIS_binary_search([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    
    print("All test cases passed!")
