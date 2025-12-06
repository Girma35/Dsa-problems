"""
LeetCode 647. Palindromic Substrings
https://leetcode.com/problems/palindromic-substrings/

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

Example 1:
    Input: s = "abc"
    Output: 3
    Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
    Input: s = "aaa"
    Output: 6
    Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

Time Complexity: O(n^2)
Space Complexity: O(1)
"""


def count_substrings(s: str) -> int:
    """
    Count palindromic substrings by expanding around each center.
    """
    count = 0
    
    def expand_around_center(left: int, right: int) -> int:
        """Count palindromes by expanding from center."""
        cnt = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            cnt += 1
            left -= 1
            right += 1
        return cnt
    
    for i in range(len(s)):
        # Odd length palindromes
        count += expand_around_center(i, i)
        # Even length palindromes
        count += expand_around_center(i, i + 1)
    
    return count


# Test cases
if __name__ == "__main__":
    # Test case 1
    assert count_substrings("abc") == 3
    
    # Test case 2
    assert count_substrings("aaa") == 6
    
    # Test case 3 - single character
    assert count_substrings("a") == 1
    
    # Test case 4 - empty string
    assert count_substrings("") == 0
    
    print("All test cases passed!")
