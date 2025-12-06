"""
LeetCode 152. Maximum Product Subarray
https://leetcode.com/problems/maximum-product-subarray/

Given an integer array nums, find a subarray that has the largest product, and 
return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:
    Input: nums = [2,3,-2,4]
    Output: 6
    Explanation: [2,3] has the largest product 6.

Example 2:
    Input: nums = [-2,0,-1]
    Output: 0
    Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


def max_product(nums: List[int]) -> int:
    """
    Find maximum product subarray by tracking both max and min products.
    We track min because a negative number can turn min into max.
    """
    if not nums:
        return 0
    
    result = nums[0]
    max_prod = nums[0]
    min_prod = nums[0]
    
    for i in range(1, len(nums)):
        num = nums[i]
        
        # When multiplied by negative, max becomes min and vice versa
        if num < 0:
            max_prod, min_prod = min_prod, max_prod
        
        max_prod = max(num, max_prod * num)
        min_prod = min(num, min_prod * num)
        
        result = max(result, max_prod)
    
    return result


# Test cases
if __name__ == "__main__":
    # Test case 1
    assert max_product([2, 3, -2, 4]) == 6
    
    # Test case 2
    assert max_product([-2, 0, -1]) == 0
    
    # Test case 3 - all positive
    assert max_product([1, 2, 3, 4]) == 24
    
    # Test case 4 - two negatives
    assert max_product([-2, -3, 4]) == 24
    
    # Test case 5 - single element
    assert max_product([-2]) == -2
    
    print("All test cases passed!")
