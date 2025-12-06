"""
LeetCode 39. Combination Sum
https://leetcode.com/problems/combination-sum/

Given an array of distinct integers candidates and a target integer target, return 
a list of all unique combinations of candidates where the chosen numbers sum to 
target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.

Example 1:
    Input: candidates = [2,3,6,7], target = 7
    Output: [[2,2,3],[7]]
    Explanation:
    2 and 3 are candidates, and 2 + 2 + 3 = 7.
    7 is a candidate, and 7 = 7.
    These are the only two combinations.

Example 2:
    Input: candidates = [2,3,5], target = 8
    Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
    Input: candidates = [2], target = 1
    Output: []

Time Complexity: O(n^(t/m)) where t = target, m = min candidate
Space Complexity: O(t/m) for recursion depth
"""

from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """
    Find all combinations that sum to target using backtracking.
    """
    result = []
    
    def backtrack(start, remaining, current):
        if remaining == 0:
            result.append(current[:])
            return
        
        if remaining < 0:
            return
        
        for i in range(start, len(candidates)):
            current.append(candidates[i])
            # Use i (not i+1) because we can reuse the same element
            backtrack(i, remaining - candidates[i], current)
            current.pop()
    
    backtrack(0, target, [])
    return result


# Test cases
if __name__ == "__main__":
    # Test case 1
    result = combination_sum([2, 3, 6, 7], 7)
    expected = [[2, 2, 3], [7]]
    assert sorted([sorted(r) for r in result]) == sorted([sorted(e) for e in expected])
    
    # Test case 2
    result = combination_sum([2, 3, 5], 8)
    expected = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    assert sorted([sorted(r) for r in result]) == sorted([sorted(e) for e in expected])
    
    # Test case 3
    assert combination_sum([2], 1) == []
    
    print("All test cases passed!")
