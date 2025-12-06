"""
LeetCode Problem 153: Find Minimum in Rotated Sorted Array
Difficulty: Medium
Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Problem:
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
For example, the array nums = [0,1,2,4,5,6,7] might become:
- [4,5,6,7,0,1,2] if it was rotated 4 times.
- [0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the 
array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Example 3:
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times.

Constraints:
- n == nums.length
- 1 <= n <= 5000
- -5000 <= nums[i] <= 5000
- All the integers of nums are unique.
- nums is sorted and rotated between 1 and n times.
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Time Complexity: O(log n)
        Space Complexity: O(1)
        
        Approach: Binary search to find the inflection point.
        """
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] > nums[right]:
                # Minimum is in right half
                left = mid + 1
            else:
                # Minimum is in left half (including mid)
                right = mid
        
        return nums[left]


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    assert solution.findMin([3, 4, 5, 1, 2]) == 1
    
    # Test case 2
    assert solution.findMin([4, 5, 6, 7, 0, 1, 2]) == 0
    
    # Test case 3
    assert solution.findMin([11, 13, 15, 17]) == 11
    
    # Test case 4
    assert solution.findMin([2, 1]) == 1
    
    print("All test cases passed!")
