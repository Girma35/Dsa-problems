"""
LeetCode 424. Longest Repeating Character Replacement
https://leetcode.com/problems/longest-repeating-character-replacement/

You are given a string s and an integer k. You can choose any character of the 
string and change it to any other uppercase English character. You can perform 
this operation at most k times.

Return the length of the longest substring containing the same letter you can 
get after performing the above operations.

Example 1:
    Input: s = "ABAB", k = 2
    Output: 4
    Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
    Input: s = "AABABBA", k = 1
    Output: 4
    Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
                 The substring "BBBB" has the longest repeating letters, which is 4.

Time Complexity: O(n)
Space Complexity: O(1) - at most 26 characters
"""


def character_replacement(s: str, k: int) -> int:
    """
    Find longest repeating character substring with k replacements.
    Uses sliding window.
    """
    from collections import defaultdict
    
    count = defaultdict(int)
    max_length = 0
    max_count = 0  # Count of most frequent character in window
    left = 0
    
    for right in range(len(s)):
        count[s[right]] += 1
        max_count = max(max_count, count[s[right]])
        
        # Window size - max_count = number of replacements needed
        # If more than k, shrink window
        while (right - left + 1) - max_count > k:
            count[s[left]] -= 1
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length


# Test cases
if __name__ == "__main__":
    # Test case 1
    assert character_replacement("ABAB", 2) == 4
    
    # Test case 2
    assert character_replacement("AABABBA", 1) == 4
    
    # Test case 3 - no replacements needed
    assert character_replacement("AAAA", 2) == 4
    
    # Test case 4 - empty string
    assert character_replacement("", 1) == 0
    
    # Test case 5 - single character
    assert character_replacement("A", 1) == 1
    
    print("All test cases passed!")
