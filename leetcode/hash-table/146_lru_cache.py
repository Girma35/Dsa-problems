"""
LeetCode Problem 146: LRU Cache
Difficulty: Medium
Link: https://leetcode.com/problems/lru-cache/

Problem:
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:
- LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
- int get(int key) Return the value of the key if the key exists, otherwise return -1.
- void put(int key, int value) Update the value of the key if the key exists. Otherwise, 
  add the key-value pair to the cache. If the number of keys exceeds the capacity from 
  this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

Example 1:
Input:
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output: [null, null, null, 1, null, -1, null, -1, 3, 4]

Constraints:
- 1 <= capacity <= 3000
- 0 <= key <= 10^4
- 0 <= value <= 10^5
- At most 2 * 10^5 calls will be made to get and put.
"""

from collections import OrderedDict


class LRUCache:
    """
    Time Complexity: O(1) for get and put
    Space Complexity: O(capacity)
    
    Approach: Use OrderedDict to maintain insertion order.
    """
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # Move to end (most recently used)
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update and move to end
            self.cache.move_to_end(key)
        self.cache[key] = value
        
        if len(self.cache) > self.capacity:
            # Remove least recently used (first item)
            self.cache.popitem(last=False)


class DoublyLinkedNode:
    """Node for doubly linked list implementation."""
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCacheManual:
    """
    Manual implementation using doubly linked list + hash map.
    """
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        # Dummy head and tail
        self.head = DoublyLinkedNode()
        self.tail = DoublyLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _add_node(self, node):
        """Add node right after head."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def _remove_node(self, node):
        """Remove node from list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _move_to_head(self, node):
        """Move existing node to head (most recent)."""
        self._remove_node(node)
        self._add_node(node)
    
    def _pop_tail(self):
        """Remove and return the tail node (LRU)."""
        node = self.tail.prev
        self._remove_node(node)
        return node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._move_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._move_to_head(node)
        else:
            node = DoublyLinkedNode(key, value)
            self.cache[key] = node
            self._add_node(node)
            
            if len(self.cache) > self.capacity:
                lru = self._pop_tail()
                del self.cache[lru.key]


# Test cases
if __name__ == "__main__":
    # Test case 1
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1)
    lRUCache.put(2, 2)
    assert lRUCache.get(1) == 1
    lRUCache.put(3, 3)  # Evicts key 2
    assert lRUCache.get(2) == -1
    lRUCache.put(4, 4)  # Evicts key 1
    assert lRUCache.get(1) == -1
    assert lRUCache.get(3) == 3
    assert lRUCache.get(4) == 4
    
    # Test manual implementation
    lRUCache2 = LRUCacheManual(2)
    lRUCache2.put(1, 1)
    lRUCache2.put(2, 2)
    assert lRUCache2.get(1) == 1
    lRUCache2.put(3, 3)
    assert lRUCache2.get(2) == -1
    lRUCache2.put(4, 4)
    assert lRUCache2.get(1) == -1
    assert lRUCache2.get(3) == 3
    assert lRUCache2.get(4) == 4
    
    print("All test cases passed!")
