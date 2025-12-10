"""
LeetCode Problem 70: Climbing Stairs
Difficulty: Easy
Link: https://leetcode.com/problems/climbing-stairs/

Problem:
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
- 1 <= n <= 45
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Approach: Dynamic Programming (Fibonacci sequence)
        dp[i] = dp[i-1] + dp[i-2]
        """
        if n <= 2:
            return n
        
        prev1, prev2 = 2, 1
        
        for _ in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        
        return prev1
    
    def climbStairs_dp(self, n: int) -> int:
        """
        Space O(n) version for clarity.
        """
        if n <= 2:
            return n
        
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    assert solution.climbStairs(2) == 2
    
    # Test case 2
    assert solution.climbStairs(3) == 3
    
    # Test case 3
    assert solution.climbStairs(1) == 1
    
    # Test case 4
    assert solution.climbStairs(5) == 8
    
    print("All test cases passed!")
