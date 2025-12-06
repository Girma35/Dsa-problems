"""
LeetCode 76. Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/

Given two strings s and t of lengths m and n respectively, return the minimum 
window substring of s such that every character in t (including duplicates) is 
included in the window. If there is no such substring, return the empty string "".

Example 1:
    Input: s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"
    Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' 
                 from string t.

Example 2:
    Input: s = "a", t = "a"
    Output: "a"

Example 3:
    Input: s = "a", t = "aa"
    Output: ""
    Explanation: Both 'a's from t must be included in the window.

Time Complexity: O(m + n)
Space Complexity: O(n)
"""

from collections import Counter


def min_window(s: str, t: str) -> str:
    """
    Find minimum window substring using sliding window with character counting.
    """
    if not s or not t:
        return ""
    
    # Count characters needed from t
    need = Counter(t)
    required = len(need)
    
    # formed = number of unique characters in current window with desired frequency
    formed = 0
    window_counts = {}
    
    left = 0
    min_len = float('inf')
    result = (0, 0)  # (start, end) of result
    
    for right in range(len(s)):
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1
        
        # Check if current character's frequency matches required
        if char in need and window_counts[char] == need[char]:
            formed += 1
        
        # Try to shrink window while it's valid
        while formed == required and left <= right:
            # Update result if this window is smaller
            if right - left + 1 < min_len:
                min_len = right - left + 1
                result = (left, right)
            
            # Remove leftmost character
            left_char = s[left]
            window_counts[left_char] -= 1
            
            if left_char in need and window_counts[left_char] < need[left_char]:
                formed -= 1
            
            left += 1
    
    return s[result[0]:result[1] + 1] if min_len != float('inf') else ""


# Test cases
if __name__ == "__main__":
    # Test case 1
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"
    
    # Test case 2
    assert min_window("a", "a") == "a"
    
    # Test case 3
    assert min_window("a", "aa") == ""
    
    # Test case 4 - t longer than s
    assert min_window("ab", "abc") == ""
    
    # Test case 5 - empty strings
    assert min_window("", "abc") == ""
    
    print("All test cases passed!")
