"""
LeetCode Problem 11: Container With Most Water
Difficulty: Medium
Link: https://leetcode.com/problems/container-with-most-water/

Problem:
You are given an integer array height of length n. There are n vertical lines drawn such 
that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container 
contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Constraints:
- n == height.length
- 2 <= n <= 10^5
- 0 <= height[i] <= 10^4
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Approach: Two pointers from both ends.
        Move the pointer with smaller height inward.
        """
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            width = right - left
            h = min(height[left], height[right])
            max_area = max(max_area, width * h)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    assert solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    
    # Test case 2
    assert solution.maxArea([1, 1]) == 1
    
    # Test case 3
    assert solution.maxArea([4, 3, 2, 1, 4]) == 16
    
    print("All test cases passed!")
