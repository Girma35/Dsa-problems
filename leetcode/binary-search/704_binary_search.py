"""
LeetCode Problem 704: Binary Search
Difficulty: Easy
Link: https://leetcode.com/problems/binary-search/

Problem:
Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. If target exists, then return its index. 
Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Constraints:
- 1 <= nums.length <= 10^4
- -10^4 < nums[i], target < 10^4
- All the integers in nums are unique.
- nums is sorted in ascending order.
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Time Complexity: O(log n)
        Space Complexity: O(1)
        
        Approach: Classic binary search.
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    assert solution.search([-1, 0, 3, 5, 9, 12], 9) == 4
    
    # Test case 2
    assert solution.search([-1, 0, 3, 5, 9, 12], 2) == -1
    
    # Test case 3
    assert solution.search([5], 5) == 0
    
    # Test case 4
    assert solution.search([5], -5) == -1
    
    print("All test cases passed!")
