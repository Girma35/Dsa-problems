"""
LeetCode 300. Longest Increasing Subsequence
https://leetcode.com/problems/longest-increasing-subsequence/

Given an integer array nums, return the length of the longest strictly increasing 
subsequence.

Example 1:
    Input: nums = [10,9,2,5,3,7,101,18]
    Output: 4
    Explanation: The longest increasing subsequence is [2,3,7,101], 
                 therefore the length is 4.

Example 2:
    Input: nums = [0,1,0,3,2,3]
    Output: 4

Example 3:
    Input: nums = [7,7,7,7,7,7,7]
    Output: 1

Time Complexity: O(n^2) for DP, O(n log n) for binary search
Space Complexity: O(n)
"""

from typing import List
import bisect


def length_of_lis(nums: List[int]) -> int:
    """
    Find LIS length using DP.
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


def length_of_lis_binary_search(nums: List[int]) -> int:
    """
    Find LIS length using binary search.
    Maintain a list where tails[i] is the smallest tail element 
    for all increasing subsequences of length i+1.
    """
    if not nums:
        return 0
    
    tails = []
    
    for num in nums:
        # Find position to insert/replace
        pos = bisect.bisect_left(tails, num)
        
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num
    
    return len(tails)


# Test cases
if __name__ == "__main__":
    # Test case 1
    assert length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    
    # Test case 2
    assert length_of_lis([0, 1, 0, 3, 2, 3]) == 4
    
    # Test case 3
    assert length_of_lis([7, 7, 7, 7, 7, 7, 7]) == 1
    
    # Test case 4 - empty array
    assert length_of_lis([]) == 0
    
    # Test case 5 - single element
    assert length_of_lis([5]) == 1
    
    # Test binary search solution
    assert length_of_lis_binary_search([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    
    print("All test cases passed!")
