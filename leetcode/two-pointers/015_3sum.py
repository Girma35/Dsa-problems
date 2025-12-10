"""
LeetCode Problem 15: 3Sum
Difficulty: Medium
Link: https://leetcode.com/problems/3sum/

Problem:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such 
that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:
- 3 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Time Complexity: O(n^2)
        Space Complexity: O(1) excluding output
        
        Approach: Sort + Two Pointers
        For each number, use two pointers to find pairs that sum to its negation.
        """
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n - 2):
            # Skip duplicates for first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for second element
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates for third element
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
        
        return result


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    result = solution.threeSum([-1, 0, 1, 2, -1, -4])
    expected = [[-1, -1, 2], [-1, 0, 1]]
    assert sorted([sorted(r) for r in result]) == sorted([sorted(e) for e in expected])
    
    # Test case 2
    assert solution.threeSum([0, 1, 1]) == []
    
    # Test case 3
    assert solution.threeSum([0, 0, 0]) == [[0, 0, 0]]
    
    print("All test cases passed!")
