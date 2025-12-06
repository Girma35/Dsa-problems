"""
LeetCode Problem 133: Clone Graph
Difficulty: Medium
Link: https://leetcode.com/problems/clone-graph/

Problem:
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

Test case format:
For simplicity, each node's value is the same as the node's index (1-indexed).

Example 1:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

Example 2:
Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list.

Example 3:
Input: adjList = []
Output: []
Explanation: This an empty graph.

Constraints:
- The number of nodes in the graph is in the range [0, 100].
- 1 <= Node.val <= 100
- Node.val is unique for each node.
- There are no repeated edges and no self-loops in the graph.
- The Graph is connected and all nodes can be visited starting from the given node.
"""

from typing import Optional
from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        Time Complexity: O(V + E)
        Space Complexity: O(V)
        
        Approach: DFS with hash map to track cloned nodes.
        """
        if not node:
            return None
        
        cloned = {}
        
        def dfs(node):
            if node in cloned:
                return cloned[node]
            
            clone = Node(node.val)
            cloned[node] = clone
            
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            
            return clone
        
        return dfs(node)
    
    def cloneGraph_bfs(self, node: Optional['Node']) -> Optional['Node']:
        """
        BFS approach.
        """
        if not node:
            return None
        
        cloned = {node: Node(node.val)}
        queue = deque([node])
        
        while queue:
            current = queue.popleft()
            
            for neighbor in current.neighbors:
                if neighbor not in cloned:
                    cloned[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                cloned[current].neighbors.append(cloned[neighbor])
        
        return cloned[node]


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Create a graph and clone it
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]
    
    clone = solution.cloneGraph(node1)
    assert clone.val == 1
    assert len(clone.neighbors) == 2
    assert clone is not node1  # Different object
    
    # Test case 2: Empty graph
    assert solution.cloneGraph(None) is None
    
    # Test case 3: Single node
    single = Node(1)
    clone_single = solution.cloneGraph(single)
    assert clone_single.val == 1
    assert clone_single.neighbors == []
    
    print("All test cases passed!")
