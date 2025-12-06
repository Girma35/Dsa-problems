"""
LeetCode 20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/

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

Time Complexity: O(n)
Space Complexity: O(n)
"""


def is_valid(s: str) -> bool:
    """
    Validate parentheses using a stack.
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
    # Test case 1
    assert is_valid("()") == True
    
    # Test case 2
    assert is_valid("()[]{}") == True
    
    # Test case 3
    assert is_valid("(]") == False
    
    # Test case 4
    assert is_valid("([)]") == False
    
    # Test case 5
    assert is_valid("{[]}") == True
    
    # Test case 6 - empty string
    assert is_valid("") == True
    
    # Test case 7 - only opening brackets
    assert is_valid("((") == False
    
    print("All test cases passed!")
