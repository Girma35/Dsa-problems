"""
LeetCode 200. Number of Islands
https://leetcode.com/problems/number-of-islands/

Given an m x n 2D binary grid which represents a map of '1's (land) and 
'0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands 
horizontally or vertically. You may assume all four edges of the grid are 
surrounded by water.

Example 1:
    Input: grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
    Output: 1

Example 2:
    Input: grid = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
    Output: 3

Time Complexity: O(m * n)
Space Complexity: O(m * n) for recursion stack in worst case
"""

from typing import List
from collections import deque


def num_islands(grid: List[List[str]]) -> int:
    """
    Count islands using DFS.
    """
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    count = 0
    
    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return
        
        grid[r][c] = '0'  # Mark as visited
        
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                dfs(r, c)
                count += 1
    
    return count


def num_islands_bfs(grid: List[List[str]]) -> int:
    """
    Count islands using BFS.
    """
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    count = 0
    
    def bfs(r, c):
        queue = deque([(r, c)])
        grid[r][c] = '0'
        
        while queue:
            row, col = queue.popleft()
            
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                    grid[nr][nc] = '0'
                    queue.append((nr, nc))
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                bfs(r, c)
                count += 1
    
    return count


# Test cases
if __name__ == "__main__":
    # Test case 1
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    assert num_islands([row[:] for row in grid]) == 1
    
    # Test case 2
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    assert num_islands([row[:] for row in grid]) == 3
    
    # Test BFS version
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    assert num_islands_bfs([row[:] for row in grid]) == 3
    
    # Test case 3 - empty grid
    assert num_islands([]) == 0
    
    print("All test cases passed!")
