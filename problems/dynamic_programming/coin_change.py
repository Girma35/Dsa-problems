"""
LeetCode 322. Coin Change
https://leetcode.com/problems/coin-change/

You are given an integer array coins representing coins of different denominations 
and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that 
amount of money cannot be made up by any combination of the coins, return -1.

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

Time Complexity: O(amount * len(coins))
Space Complexity: O(amount)
"""

from typing import List


def coin_change(coins: List[int], amount: int) -> int:
    """
    Find minimum coins using bottom-up DP.
    dp[i] = minimum coins needed to make amount i
    """
    # Initialize with amount + 1 (impossible value)
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != amount + 1 else -1


def coin_change_bfs(coins: List[int], amount: int) -> int:
    """
    Find minimum coins using BFS.
    Each level represents using one more coin.
    """
    if amount == 0:
        return 0
    
    from collections import deque
    
    visited = set([0])
    queue = deque([0])
    level = 0
    
    while queue:
        level += 1
        level_size = len(queue)
        
        for _ in range(level_size):
            current = queue.popleft()
            
            for coin in coins:
                new_amount = current + coin
                
                if new_amount == amount:
                    return level
                
                if new_amount < amount and new_amount not in visited:
                    visited.add(new_amount)
                    queue.append(new_amount)
    
    return -1


# Test cases
if __name__ == "__main__":
    # Test case 1
    assert coin_change([1, 2, 5], 11) == 3
    
    # Test case 2
    assert coin_change([2], 3) == -1
    
    # Test case 3
    assert coin_change([1], 0) == 0
    
    # Test case 4
    assert coin_change([1, 2, 5], 100) == 20
    
    # Test BFS solution
    assert coin_change_bfs([1, 2, 5], 11) == 3
    
    print("All test cases passed!")
