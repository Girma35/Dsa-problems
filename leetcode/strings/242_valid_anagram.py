"""
LeetCode Problem 242: Valid Anagram
Difficulty: Easy
Link: https://leetcode.com/problems/valid-anagram/

Problem:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word 
or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
- 1 <= s.length, t.length <= 5 * 10^4
- s and t consist of lowercase English letters.
"""

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Time Complexity: O(n)
        Space Complexity: O(1) - at most 26 characters
        
        Approach: Count character frequencies and compare.
        """
        if len(s) != len(t):
            return False
        
        return Counter(s) == Counter(t)
    
    def isAnagram_manual(self, s: str, t: str) -> bool:
        """
        Alternative approach without Counter.
        """
        if len(s) != len(t):
            return False
        
        count = {}
        
        for c in s:
            count[c] = count.get(c, 0) + 1
        
        for c in t:
            if c not in count:
                return False
            count[c] -= 1
            if count[c] == 0:
                del count[c]
        
        return len(count) == 0


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    assert solution.isAnagram("anagram", "nagaram") == True
    
    # Test case 2
    assert solution.isAnagram("rat", "car") == False
    
    # Test case 3
    assert solution.isAnagram("a", "a") == True
    
    # Test case 4
    assert solution.isAnagram("ab", "a") == False
    
    print("All test cases passed!")
