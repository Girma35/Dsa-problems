"""
LeetCode Problem 238: Product of Array Except Self
Difficulty: Medium
Link: https://leetcode.com/problems/product-of-array-except-self/

Problem:
Given an integer array nums, return an array answer such that answer[i] is equal to 
the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
- 2 <= nums.length <= 10^5
- -30 <= nums[i] <= 30
- The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Time Complexity: O(n)
        Space Complexity: O(1) (excluding output array)
        
        Approach: Use prefix and suffix products.
        First pass: Calculate prefix products.
        Second pass: Calculate suffix products and multiply with prefix.
        """
        n = len(nums)
        result = [1] * n
        
        # Calculate prefix products
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        
        # Calculate suffix products and multiply
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        
        return result


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    assert solution.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    
    # Test case 2
    assert solution.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    
    # Test case 3
    assert solution.productExceptSelf([2, 3]) == [3, 2]
    
    print("All test cases passed!")
