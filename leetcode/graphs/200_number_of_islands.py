"""
LeetCode Problem 200: Number of Islands
Difficulty: Medium
Link: https://leetcode.com/problems/number-of-islands/

Problem:
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally 
or vertically. You may assume all four edges of the grid are all surrounded by water.

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

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 300
- grid[i][j] is '0' or '1'.
"""

from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Time Complexity: O(m * n)
        Space Complexity: O(m * n) in worst case for recursion stack
        
        Approach: DFS to mark visited land cells.
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
                    count += 1
                    dfs(r, c)
        
        return count
    
    def numIslands_bfs(self, grid: List[List[str]]) -> int:
        """
        BFS approach.
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
                    count += 1
                    bfs(r, c)
        
        return count


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    assert solution.numIslands(grid1) == 1
    
    # Test case 2
    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    assert solution.numIslands(grid2) == 3
    
    # Test case 3: Empty grid
    assert solution.numIslands([]) == 0
    
    print("All test cases passed!")
