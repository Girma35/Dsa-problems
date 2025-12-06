"""
LeetCode 153. Find Minimum in Rotated Sorted Array
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Suppose an array of length n sorted in ascending order is rotated between 1 and 
n times. Given the sorted rotated array nums of unique elements, return the 
minimum element of this array.

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

Time Complexity: O(log n)
Space Complexity: O(1)
"""

from typing import List


def find_min(nums: List[int]) -> int:
    """
    Find minimum element using binary search.
    The minimum is where the rotation point is.
    """
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        # If mid element is greater than right element,
        # minimum is in the right half
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            # Minimum is in the left half (including mid)
            right = mid
    
    return nums[left]


# Test cases
if __name__ == "__main__":
    # Test case 1
    assert find_min([3, 4, 5, 1, 2]) == 1
    
    # Test case 2
    assert find_min([4, 5, 6, 7, 0, 1, 2]) == 0
    
    # Test case 3 - not rotated
    assert find_min([11, 13, 15, 17]) == 11
    
    # Test case 4 - single element
    assert find_min([1]) == 1
    
    # Test case 5 - two elements
    assert find_min([2, 1]) == 1
    
    print("All test cases passed!")
