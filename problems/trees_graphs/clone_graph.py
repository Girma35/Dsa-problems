"""
LeetCode 133. Clone Graph
https://leetcode.com/problems/clone-graph/

Given a reference of a node in a connected undirected graph, return a deep copy 
(clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its 
neighbors.

Example 1:
    Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
    Output: [[2,4],[1,3],[2,4],[1,3]]
    Explanation: There are 4 nodes in the graph.
    1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
    2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
    3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
    4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

Time Complexity: O(V + E)
Space Complexity: O(V)
"""

from typing import Optional
from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: Optional[Node]) -> Optional[Node]:
    """
    Clone graph using DFS with hash map for visited nodes.
    """
    if not node:
        return None
    
    cloned = {}  # Original node -> Cloned node
    
    def dfs(n):
        if n in cloned:
            return cloned[n]
        
        # Create clone
        clone = Node(n.val)
        cloned[n] = clone
        
        # Clone neighbors
        for neighbor in n.neighbors:
            clone.neighbors.append(dfs(neighbor))
        
        return clone
    
    return dfs(node)


def clone_graph_bfs(node: Optional[Node]) -> Optional[Node]:
    """
    Clone graph using BFS.
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
    # Test case 1: Graph with 4 nodes
    # 1 -- 2
    # |    |
    # 4 -- 3
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]
    
    cloned = clone_graph(node1)
    assert cloned.val == 1
    assert cloned is not node1  # Different object
    assert len(cloned.neighbors) == 2
    
    # Test case 2: Empty graph
    assert clone_graph(None) is None
    
    # Test case 3: Single node
    single = Node(1)
    cloned_single = clone_graph(single)
    assert cloned_single.val == 1
    assert cloned_single is not single
    
    print("All test cases passed!")
