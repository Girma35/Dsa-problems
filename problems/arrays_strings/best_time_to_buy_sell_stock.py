"""
LeetCode 121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You are given an array prices where prices[i] is the price of a given stock on 
the ith day.

You want to maximize your profit by choosing a single day to buy one stock and 
choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot 
achieve any profit, return 0.

Example 1:
    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), 
                 profit = 6-1 = 5.

Example 2:
    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transactions are done and the max profit = 0.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


def max_profit(prices: List[int]) -> int:
    """
    Find maximum profit by tracking minimum price seen so far.
    """
    if not prices:
        return 0
    
    min_price = float('inf')
    max_profit_val = 0
    
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            max_profit_val = max(max_profit_val, price - min_price)
    
    return max_profit_val


# Test cases
if __name__ == "__main__":
    # Test case 1
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    
    # Test case 2
    assert max_profit([7, 6, 4, 3, 1]) == 0
    
    # Test case 3 - empty array
    assert max_profit([]) == 0
    
    # Test case 4 - single element
    assert max_profit([5]) == 0
    
    print("All test cases passed!")
