"""
LeetCode 11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/

You are given an integer array height of length n. There are n vertical lines 
drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the 
container contains the most water.

Return the maximum amount of water a container can store.

Example 1:
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: The vertical lines are drawn at positions 0-8. The max area is 
                 between lines at index 1 and 8. Area = min(8,7) * (8-1) = 49

Example 2:
    Input: height = [1,1]
    Output: 1

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


def max_area(height: List[int]) -> int:
    """
    Find maximum water container using two pointers.
    Move the pointer with smaller height inward.
    """
    left, right = 0, len(height) - 1
    max_water = 0
    
    while left < right:
        # Calculate current water
        width = right - left
        water = width * min(height[left], height[right])
        max_water = max(max_water, water)
        
        # Move the pointer with smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_water


# Test cases
if __name__ == "__main__":
    # Test case 1
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    
    # Test case 2
    assert max_area([1, 1]) == 1
    
    # Test case 3 - increasing heights
    assert max_area([1, 2, 3, 4, 5]) == 6
    
    # Test case 4 - decreasing heights
    assert max_area([5, 4, 3, 2, 1]) == 6
    
    print("All test cases passed!")
