"""
LeetCode Problem 121: Best Time to Buy and Sell Stock
Difficulty: Easy
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Problem:
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing 
a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve 
any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: No transactions are done and the max profit = 0.

Constraints:
- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Approach: Track minimum price seen so far and maximum profit.
        """
        if not prices:
            return 0
        
        min_price = prices[0]
        max_profit = 0
        
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        
        return max_profit


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    
    # Test case 2
    assert solution.maxProfit([7, 6, 4, 3, 1]) == 0
    
    # Test case 3: Single element
    assert solution.maxProfit([1]) == 0
    
    # Test case 4: Increasing prices
    assert solution.maxProfit([1, 2, 3, 4, 5]) == 4
    
    print("All test cases passed!")
