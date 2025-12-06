"""
LeetCode 198. House Robber
https://leetcode.com/problems/house-robber/

You are a professional robber planning to rob houses along a street. Each house 
has a certain amount of money stashed, the only constraint stopping you from 
robbing each of them is that adjacent houses have security systems connected and 
it will automatically contact the police if two adjacent houses were broken into 
on the same night.

Given an integer array nums representing the amount of money of each house, return 
the maximum amount of money you can rob tonight without alerting the police.

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

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


def rob(nums: List[int]) -> int:
    """
    Find maximum amount using DP with O(1) space.
    At each house, decide: rob this house or skip it.
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    # Track max money from previous two houses
    prev2 = 0  # Two houses back
    prev1 = 0  # Previous house
    
    for num in nums:
        current = max(prev2 + num, prev1)
        prev2 = prev1
        prev1 = current
    
    return prev1


def rob_dp_array(nums: List[int]) -> int:
    """
    Find maximum amount using explicit DP array.
    dp[i] = maximum amount robbed from first i houses
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
    
    return dp[n - 1]


# Test cases
if __name__ == "__main__":
    # Test case 1
    assert rob([1, 2, 3, 1]) == 4
    
    # Test case 2
    assert rob([2, 7, 9, 3, 1]) == 12
    
    # Test case 3 - empty array
    assert rob([]) == 0
    
    # Test case 4 - single house
    assert rob([5]) == 5
    
    # Test case 5 - two houses
    assert rob([1, 2]) == 2
    
    # Test DP array solution
    assert rob_dp_array([2, 7, 9, 3, 1]) == 12
    
    print("All test cases passed!")
