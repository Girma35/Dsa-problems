"""
LeetCode 213. House Robber II
https://leetcode.com/problems/house-robber-ii/

You are a professional robber planning to rob houses along a street. Each house 
has a certain amount of money stashed. All houses at this place are arranged in 
a circle. That means the first house is the neighbor of the last one.

Given an integer array nums representing the amount of money of each house, return 
the maximum amount of money you can rob tonight without alerting the police.

Example 1:
    Input: nums = [2,3,2]
    Output: 3
    Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), 
                 because they are adjacent houses.

Example 2:
    Input: nums = [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
                 Total amount you can rob = 1 + 3 = 4.

Example 3:
    Input: nums = [1,2,3]
    Output: 3

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


def rob(nums: List[int]) -> int:
    """
    Since houses are in a circle, we can't rob both first and last house.
    Solution: Max of (rob houses 0 to n-2) and (rob houses 1 to n-1)
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums)
    
    def rob_linear(houses):
        prev2, prev1 = 0, 0
        for money in houses:
            current = max(prev2 + money, prev1)
            prev2 = prev1
            prev1 = current
        return prev1
    
    # Rob houses 0 to n-2 OR houses 1 to n-1
    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))


# Test cases
if __name__ == "__main__":
    # Test case 1
    assert rob([2, 3, 2]) == 3
    
    # Test case 2
    assert rob([1, 2, 3, 1]) == 4
    
    # Test case 3
    assert rob([1, 2, 3]) == 3
    
    # Test case 4 - empty array
    assert rob([]) == 0
    
    # Test case 5 - single house
    assert rob([5]) == 5
    
    # Test case 6 - two houses
    assert rob([1, 2]) == 2
    
    print("All test cases passed!")
