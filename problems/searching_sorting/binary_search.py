"""
LeetCode 704. Binary Search
https://leetcode.com/problems/binary-search/

Given an array of integers nums which is sorted in ascending order, and an integer 
target, write a function to search target in nums. If target exists, then return 
its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [-1,0,3,5,9,12], target = 9
    Output: 4
    Explanation: 9 exists in nums and its index is 4

Example 2:
    Input: nums = [-1,0,3,5,9,12], target = 2
    Output: -1
    Explanation: 2 does not exist in nums so return -1

Time Complexity: O(log n)
Space Complexity: O(1)
"""

from typing import List


def search(nums: List[int], target: int) -> int:
    """
    Binary search implementation.
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def search_recursive(nums: List[int], target: int, left: int = None, right: int = None) -> int:
    """
    Recursive binary search.
    """
    if left is None:
        left = 0
    if right is None:
        right = len(nums) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return search_recursive(nums, target, mid + 1, right)
    else:
        return search_recursive(nums, target, left, mid - 1)


# Test cases
if __name__ == "__main__":
    # Test case 1
    assert search([-1, 0, 3, 5, 9, 12], 9) == 4
    
    # Test case 2
    assert search([-1, 0, 3, 5, 9, 12], 2) == -1
    
    # Test case 3 - single element found
    assert search([5], 5) == 0
    
    # Test case 4 - single element not found
    assert search([5], 2) == -1
    
    # Test recursive version
    assert search_recursive([-1, 0, 3, 5, 9, 12], 9) == 4
    
    print("All test cases passed!")
