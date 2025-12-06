"""
LeetCode 5. Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, return the longest palindromic substring in s.

Example 1:
    Input: s = "babad"
    Output: "bab"
    Explanation: "aba" is also a valid answer.

Example 2:
    Input: s = "cbbd"
    Output: "bb"

Time Complexity: O(n^2)
Space Complexity: O(1) for expand around center
"""


def longest_palindrome(s: str) -> str:
    """
    Find longest palindromic substring by expanding around center.
    """
    if not s:
        return ""
    
    start, end = 0, 0
    
    def expand_around_center(left: int, right: int) -> int:
        """Expand and return the length of palindrome."""
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    
    for i in range(len(s)):
        # Odd length palindrome (single center)
        len1 = expand_around_center(i, i)
        # Even length palindrome (two centers)
        len2 = expand_around_center(i, i + 1)
        
        max_len = max(len1, len2)
        
        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2
    
    return s[start:end + 1]


def longest_palindrome_dp(s: str) -> str:
    """
    Find longest palindromic substring using dynamic programming.
    dp[i][j] = True if s[i:j+1] is a palindrome
    """
    n = len(s)
    if n < 2:
        return s
    
    dp = [[False] * n for _ in range(n)]
    start = 0
    max_length = 1
    
    # All single characters are palindromes
    for i in range(n):
        dp[i][i] = True
    
    # Check for length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_length = 2
    
    # Check for lengths > 2
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if length > max_length:
                    start = i
                    max_length = length
    
    return s[start:start + max_length]


# Test cases
if __name__ == "__main__":
    # Test case 1
    result = longest_palindrome("babad")
    assert result in ["bab", "aba"]
    
    # Test case 2
    assert longest_palindrome("cbbd") == "bb"
    
    # Test case 3 - single character
    assert longest_palindrome("a") == "a"
    
    # Test case 4 - empty string
    assert longest_palindrome("") == ""
    
    # Test case 5 - all same characters
    assert longest_palindrome("aaaa") == "aaaa"
    
    # Test DP solution
    result = longest_palindrome_dp("babad")
    assert result in ["bab", "aba"]
    
    print("All test cases passed!")
