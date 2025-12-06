"""
LeetCode 33. Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/

There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown 
pivot index.

Given the array nums after the possible rotation and an integer target, return 
the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4

Example 2:
    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1

Example 3:
    Input: nums = [1], target = 0
    Output: -1

Time Complexity: O(log n)
Space Complexity: O(1)
"""

from typing import List


def search(nums: List[int], target: int) -> int:
    """
    Search for target in rotated sorted array using modified binary search.
    """
    if not nums:
        return -1
    
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        # Check which half is sorted
        if nums[left] <= nums[mid]:
            # Left half is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1


# Test cases
if __name__ == "__main__":
    # Test case 1
    assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    
    # Test case 2
    assert search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    
    # Test case 3
    assert search([1], 0) == -1
    
    # Test case 4 - target at beginning
    assert search([4, 5, 6, 7, 0, 1, 2], 4) == 0
    
    # Test case 5 - target at end
    assert search([4, 5, 6, 7, 0, 1, 2], 2) == 6
    
    print("All test cases passed!")
