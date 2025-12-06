"""
LeetCode Problem 322: Coin Change
Difficulty: Medium
Link: https://leetcode.com/problems/coin-change/

Problem:
You are given an integer array coins representing coins of different denominations and 
an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount 
of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0

Constraints:
- 1 <= coins.length <= 12
- 1 <= coins[i] <= 2^31 - 1
- 0 <= amount <= 10^4
"""

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Time Complexity: O(amount * len(coins))
        Space Complexity: O(amount)
        
        Approach: Bottom-up Dynamic Programming
        dp[i] = minimum coins needed to make amount i
        """
        # Initialize with amount + 1 (impossible value)
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[amount] if dp[amount] <= amount else -1


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    assert solution.coinChange([1, 2, 5], 11) == 3
    
    # Test case 2
    assert solution.coinChange([2], 3) == -1
    
    # Test case 3
    assert solution.coinChange([1], 0) == 0
    
    # Test case 4
    assert solution.coinChange([1], 2) == 2
    
    print("All test cases passed!")
