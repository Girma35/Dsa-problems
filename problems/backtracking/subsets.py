"""
LeetCode 78. Subsets
https://leetcode.com/problems/subsets/

Given an integer array nums of unique elements, return all possible subsets (the 
power set).

The solution set must not contain duplicate subsets. Return the solution in any 
order.

Example 1:
    Input: nums = [1,2,3]
    Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
    Input: nums = [0]
    Output: [[],[0]]

Time Complexity: O(n * 2^n)
Space Complexity: O(n) for recursion stack
"""

from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    """
    Generate all subsets using backtracking.
    """
    result = []
    
    def backtrack(start, current):
        # Add current subset to result
        result.append(current[:])
        
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()
    
    backtrack(0, [])
    return result


def subsets_iterative(nums: List[int]) -> List[List[int]]:
    """
    Generate all subsets iteratively.
    Start with empty set, add each number to all existing subsets.
    """
    result = [[]]
    
    for num in nums:
        result += [subset + [num] for subset in result]
    
    return result


def subsets_bitmask(nums: List[int]) -> List[List[int]]:
    """
    Generate all subsets using bit manipulation.
    Each subset can be represented by a bitmask.
    """
    n = len(nums)
    result = []
    
    for mask in range(2 ** n):
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(nums[i])
        result.append(subset)
    
    return result


# Test cases
if __name__ == "__main__":
    # Test case 1
    result = subsets([1, 2, 3])
    expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    assert len(result) == len(expected)
    assert all(sorted(s) in [sorted(e) for e in expected] for s in result)
    
    # Test case 2
    assert sorted(subsets([0])) == sorted([[], [0]])
    
    # Test iterative solution
    result = subsets_iterative([1, 2])
    assert len(result) == 4
    
    # Test bitmask solution
    result = subsets_bitmask([1, 2])
    assert len(result) == 4
    
    print("All test cases passed!")
