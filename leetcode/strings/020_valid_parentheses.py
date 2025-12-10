"""
LeetCode Problem 20: Valid Parentheses
Difficulty: Easy
Link: https://leetcode.com/problems/valid-parentheses/

Problem:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Constraints:
- 1 <= s.length <= 10^4
- s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Approach: Use a stack to match brackets.
        """
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping:
                # Closing bracket
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                # Opening bracket
                stack.append(char)
        
        return len(stack) == 0


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    assert solution.isValid("()") == True
    
    # Test case 2
    assert solution.isValid("()[]{}") == True
    
    # Test case 3
    assert solution.isValid("(]") == False
    
    # Test case 4
    assert solution.isValid("([)]") == False
    
    # Test case 5
    assert solution.isValid("{[]}") == True
    
    print("All test cases passed!")
