"""
LeetCode 3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without repeating 
characters.

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
    Notice that the answer must be a substring, "pwke" is a subsequence.

Time Complexity: O(n)
Space Complexity: O(min(n, m)) where m is the character set size
"""


def length_of_longest_substring(s: str) -> int:
    """
    Find longest substring without repeating characters using sliding window.
    """
    char_index = {}  # Last index of each character
    max_length = 0
    left = 0
    
    for right, char in enumerate(s):
        # If character was seen and is in current window, move left pointer
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        
        char_index[char] = right
        max_length = max(max_length, right - left + 1)
    
    return max_length


def length_of_longest_substring_set(s: str) -> int:
    """
    Alternative using a set.
    """
    char_set = set()
    max_length = 0
    left = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length


# Test cases
if __name__ == "__main__":
    # Test case 1
    assert length_of_longest_substring("abcabcbb") == 3
    
    # Test case 2
    assert length_of_longest_substring("bbbbb") == 1
    
    # Test case 3
    assert length_of_longest_substring("pwwkew") == 3
    
    # Test case 4 - empty string
    assert length_of_longest_substring("") == 0
    
    # Test case 5 - single character
    assert length_of_longest_substring("a") == 1
    
    # Test set solution
    assert length_of_longest_substring_set("abcabcbb") == 3
    
    print("All test cases passed!")
