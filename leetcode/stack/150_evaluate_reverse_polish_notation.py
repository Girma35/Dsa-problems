"""
LeetCode Problem 150: Evaluate Reverse Polish Notation
Difficulty: Medium
Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/

Problem:
You are given an array of strings tokens that represents an arithmetic expression in 
Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:
- The valid operators are '+', '-', '*', and '/'.
- Each operand may be an integer or another expression.
- The division between two integers always truncates toward zero.
- There will not be any division by zero.
- The input represents a valid arithmetic expression in reverse polish notation.
- The answer and all the intermediate calculations can be represented in a 32-bit integer.

Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22

Constraints:
- 1 <= tokens.length <= 10^4
- tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
"""

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Approach: Use a stack to evaluate the expression.
        """
        stack = []
        operators = {'+', '-', '*', '/'}
        
        for token in tokens:
            if token in operators:
                b = stack.pop()
                a = stack.pop()
                
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    # Truncate toward zero
                    stack.append(int(a / b))
            else:
                stack.append(int(token))
        
        return stack[0]


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    assert solution.evalRPN(["2", "1", "+", "3", "*"]) == 9
    
    # Test case 2
    assert solution.evalRPN(["4", "13", "5", "/", "+"]) == 6
    
    # Test case 3
    assert solution.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
    
    print("All test cases passed!")
