"""
LeetCode 739. Daily Temperatures
https://leetcode.com/problems/daily-temperatures/

Given an array of integers temperatures represents the daily temperatures, return 
an array answer such that answer[i] is the number of days you have to wait after 
the ith day to get a warmer temperature.

If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
    Input: temperatures = [73,74,75,71,69,72,76,73]
    Output: [1,1,4,2,1,1,0,0]

Example 2:
    Input: temperatures = [30,40,50,60]
    Output: [1,1,1,0]

Example 3:
    Input: temperatures = [30,60,90]
    Output: [1,1,0]

Time Complexity: O(n)
Space Complexity: O(n)

Algorithm: Monotonic Decreasing Stack
"""

from typing import List


def daily_temperatures(temperatures: List[int]) -> List[int]:
    """
    Find days until warmer temperature using monotonic stack.
    Stack stores indices of temperatures waiting for warmer day.
    """
    n = len(temperatures)
    result = [0] * n
    stack = []  # Stack of indices
    
    for i, temp in enumerate(temperatures):
        # Pop all temperatures smaller than current
        while stack and temperatures[stack[-1]] < temp:
            prev_idx = stack.pop()
            result[prev_idx] = i - prev_idx
        stack.append(i)
    
    return result


# Test cases
if __name__ == "__main__":
    # Test case 1
    assert daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    
    # Test case 2
    assert daily_temperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
    
    # Test case 3
    assert daily_temperatures([30, 60, 90]) == [1, 1, 0]
    
    # Test case 4 - decreasing temperatures
    assert daily_temperatures([90, 80, 70]) == [0, 0, 0]
    
    # Test case 5 - single element
    assert daily_temperatures([73]) == [0]
    
    print("All test cases passed!")
