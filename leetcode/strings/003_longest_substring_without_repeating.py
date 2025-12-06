"""
LeetCode Problem 3: Longest Substring Without Repeating Characters
Difficulty: Medium
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Problem:
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.

Constraints:
- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(min(m, n)) where m is the size of charset
        
        Approach: Sliding window with hash map to track character indices.
        """
        char_index = {}
        max_length = 0
        start = 0
        
        for end, char in enumerate(s):
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1
            
            char_index[char] = end
            max_length = max(max_length, end - start + 1)
        
        return max_length


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    assert solution.lengthOfLongestSubstring("abcabcbb") == 3
    
    # Test case 2
    assert solution.lengthOfLongestSubstring("bbbbb") == 1
    
    # Test case 3
    assert solution.lengthOfLongestSubstring("pwwkew") == 3
    
    # Test case 4: Empty string
    assert solution.lengthOfLongestSubstring("") == 0
    
    # Test case 5
    assert solution.lengthOfLongestSubstring("aab") == 2
    
    print("All test cases passed!")
