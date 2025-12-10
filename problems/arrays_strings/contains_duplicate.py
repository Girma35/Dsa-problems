"""
LeetCode 217. Contains Duplicate
https://leetcode.com/problems/contains-duplicate/

Given an integer array nums, return true if any value appears at least twice 
in the array, and return false if every element is distinct.

Example 1:
    Input: nums = [1,2,3,1]
    Output: true

Example 2:
    Input: nums = [1,2,3,4]
    Output: false

Example 3:
    Input: nums = [1,1,1,3,3,4,3,2,4,2]
    Output: true

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    """
    Check if array contains any duplicates using a set.
    """
    seen = set()
    
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    
    return False


def contains_duplicate_pythonic(nums: List[int]) -> bool:
    """
    Pythonic one-liner solution.
    """
    return len(nums) != len(set(nums))


# Test cases
if __name__ == "__main__":
    # Test case 1
    assert contains_duplicate([1, 2, 3, 1]) == True
    
    # Test case 2
    assert contains_duplicate([1, 2, 3, 4]) == False
    
    # Test case 3
    assert contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
    
    # Test case 4 - empty array
    assert contains_duplicate([]) == False
    
    # Test pythonic solution
    assert contains_duplicate_pythonic([1, 2, 3, 1]) == True
    assert contains_duplicate_pythonic([1, 2, 3, 4]) == False
    
    print("All test cases passed!")
