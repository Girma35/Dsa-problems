"""
LeetCode Problem 207: Course Schedule
Difficulty: Medium
Link: https://leetcode.com/problems/course-schedule/

Problem:
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you 
must take course bi first if you want to take course ai.

Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should 
also have finished course 1. So it is impossible.

Constraints:
- 1 <= numCourses <= 2000
- 0 <= prerequisites.length <= 5000
- prerequisites[i].length == 2
- 0 <= ai, bi < numCourses
- All the pairs prerequisites[i] are unique.
"""

from typing import List
from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Time Complexity: O(V + E)
        Space Complexity: O(V + E)
        
        Approach: Topological sort using DFS cycle detection.
        """
        # Build adjacency list
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        # States: 0 = unvisited, 1 = visiting, 2 = visited
        state = [0] * numCourses
        
        def has_cycle(course):
            if state[course] == 1:  # Cycle detected
                return True
            if state[course] == 2:  # Already processed
                return False
            
            state[course] = 1  # Mark as visiting
            
            for next_course in graph[course]:
                if has_cycle(next_course):
                    return True
            
            state[course] = 2  # Mark as visited
            return False
        
        for course in range(numCourses):
            if has_cycle(course):
                return False
        
        return True
    
    def canFinish_bfs(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        BFS approach (Kahn's algorithm).
        """
        # Build adjacency list and in-degree count
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1
        
        # Start with courses having no prerequisites
        queue = deque([c for c in range(numCourses) if in_degree[c] == 0])
        completed = 0
        
        while queue:
            course = queue.popleft()
            completed += 1
            
            for next_course in graph[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        
        return completed == numCourses


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    assert solution.canFinish(2, [[1, 0]]) == True
    
    # Test case 2
    assert solution.canFinish(2, [[1, 0], [0, 1]]) == False
    
    # Test case 3: No prerequisites
    assert solution.canFinish(3, []) == True
    
    # Test case 4
    assert solution.canFinish(4, [[1, 0], [2, 1], [3, 2]]) == True
    
    print("All test cases passed!")
