"""
LeetCode Problem 217: Contains Duplicate
Difficulty: Easy
Link: https://leetcode.com/problems/contains-duplicate/

Problem:
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Approach: Use a set to track seen numbers.
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    assert solution.containsDuplicate([1, 2, 3, 1]) == True
    
    # Test case 2
    assert solution.containsDuplicate([1, 2, 3, 4]) == False
    
    # Test case 3
    assert solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
    
    print("All test cases passed!")
