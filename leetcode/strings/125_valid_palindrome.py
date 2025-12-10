"""
LeetCode Problem 125: Valid Palindrome
Difficulty: Easy
Link: https://leetcode.com/problems/valid-palindrome/

Problem:
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.

Constraints:
- 1 <= s.length <= 2 * 10^5
- s consists only of printable ASCII characters.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Approach: Two pointers from both ends, skip non-alphanumeric characters.
        """
        left, right = 0, len(s) - 1
        
        while left < right:
            # Skip non-alphanumeric from left
            while left < right and not s[left].isalnum():
                left += 1
            # Skip non-alphanumeric from right
            while left < right and not s[right].isalnum():
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    assert solution.isPalindrome("A man, a plan, a canal: Panama") == True
    
    # Test case 2
    assert solution.isPalindrome("race a car") == False
    
    # Test case 3
    assert solution.isPalindrome(" ") == True
    
    # Test case 4
    assert solution.isPalindrome("0P") == False
    
    print("All test cases passed!")
