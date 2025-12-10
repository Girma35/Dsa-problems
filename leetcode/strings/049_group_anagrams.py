"""
LeetCode Problem 49: Group Anagrams
Difficulty: Medium
Link: https://leetcode.com/problems/group-anagrams/

Problem:
Given an array of strings strs, group the anagrams together. You can return the answer 
in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word 
or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
- 1 <= strs.length <= 10^4
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters.
"""

from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Time Complexity: O(n * k * log(k)) where n is number of strings, k is max length
        Space Complexity: O(n * k)
        
        Approach: Group strings by their sorted version as key.
        """
        groups = defaultdict(list)
        
        for s in strs:
            key = tuple(sorted(s))
            groups[key].append(s)
        
        return list(groups.values())
    
    def groupAnagrams_count(self, strs: List[str]) -> List[List[str]]:
        """
        Alternative approach: Use character count as key.
        Time Complexity: O(n * k)
        """
        groups = defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            groups[tuple(count)].append(s)
        
        return list(groups.values())


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    result = solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    # Sort for comparison
    result = [sorted(group) for group in result]
    expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    expected = [sorted(group) for group in expected]
    assert sorted([tuple(g) for g in result]) == sorted([tuple(g) for g in expected])
    
    # Test case 2
    assert solution.groupAnagrams([""]) == [[""]]
    
    # Test case 3
    assert solution.groupAnagrams(["a"]) == [["a"]]
    
    print("All test cases passed!")
