"""
LeetCode 70. Climbing Stairs
https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you 
climb to the top?

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

Time Complexity: O(n)
Space Complexity: O(1) for optimized solution
"""


def climb_stairs(n: int) -> int:
    """
    Count distinct ways to climb stairs using DP.
    This is essentially the Fibonacci sequence.
    """
    if n <= 2:
        return n
    
    # Only need to track last two values
    prev1, prev2 = 2, 1
    
    for _ in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    
    return prev1


def climb_stairs_dp(n: int) -> int:
    """
    Count distinct ways using explicit DP array.
    dp[i] = number of ways to reach step i
    """
    if n <= 2:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]


def climb_stairs_recursive(n: int, memo: dict = None) -> int:
    """
    Count distinct ways using memoization.
    """
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 2:
        return n
    
    memo[n] = climb_stairs_recursive(n - 1, memo) + climb_stairs_recursive(n - 2, memo)
    return memo[n]


# Test cases
if __name__ == "__main__":
    # Test case 1
    assert climb_stairs(2) == 2
    
    # Test case 2
    assert climb_stairs(3) == 3
    
    # Test case 3
    assert climb_stairs(1) == 1
    
    # Test case 4
    assert climb_stairs(5) == 8
    
    # Test DP solution
    assert climb_stairs_dp(5) == 8
    
    # Test recursive solution
    assert climb_stairs_recursive(5) == 8
    
    print("All test cases passed!")
