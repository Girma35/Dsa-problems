"""
LeetCode Problem 198: House Robber
Difficulty: Medium
Link: https://leetcode.com/problems/house-robber/

Problem:
You are a professional robber planning to rob houses along a street. Each house has a 
certain amount of money stashed, the only constraint stopping you from robbing each of 
them is that adjacent houses have security systems connected and it will automatically 
contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the 
maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 400
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Approach: Dynamic Programming
        At each house, decide to rob or skip.
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        prev2 = nums[0]
        prev1 = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            current = max(prev1, prev2 + nums[i])
            prev2 = prev1
            prev1 = current
        
        return prev1


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    assert solution.rob([1, 2, 3, 1]) == 4
    
    # Test case 2
    assert solution.rob([2, 7, 9, 3, 1]) == 12
    
    # Test case 3
    assert solution.rob([1]) == 1
    
    # Test case 4
    assert solution.rob([2, 1]) == 2
    
    print("All test cases passed!")
