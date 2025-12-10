"""
LeetCode Problem 128: Longest Consecutive Sequence
Difficulty: Medium
Link: https://leetcode.com/problems/longest-consecutive-sequence/

Problem:
Given an unsorted array of integers nums, return the length of the longest consecutive 
elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:
- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Approach: Use a set to check consecutive numbers in O(1).
        Only start counting from numbers that are the start of a sequence.
        """
        if not nums:
            return 0
        
        num_set = set(nums)
        max_length = 0
        
        for num in num_set:
            # Only start counting if this is the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_length = 1
                
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1
                
                max_length = max(max_length, current_length)
        
        return max_length


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    assert solution.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    
    # Test case 2
    assert solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    
    # Test case 3: Empty array
    assert solution.longestConsecutive([]) == 0
    
    # Test case 4: Single element
    assert solution.longestConsecutive([1]) == 1
    
    print("All test cases passed!")
