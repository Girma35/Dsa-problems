"""
LeetCode 141. Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/

Given head, the head of a linked list, determine if the linked list has a cycle 
in it.

There is a cycle in a linked list if there is some node in the list that can be 
reached again by continuously following the next pointer.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
    Input: head = [3,2,0,-4], pos = 1
    Output: true
    Explanation: There is a cycle in the linked list, where the tail connects to 
                 the 1st node (0-indexed).

Example 2:
    Input: head = [1,2], pos = 0
    Output: true
    Explanation: There is a cycle in the linked list, where the tail connects to 
                 the 0th node.

Example 3:
    Input: head = [1], pos = -1
    Output: false
    Explanation: There is no cycle in the linked list.

Time Complexity: O(n)
Space Complexity: O(1)

Algorithm: Floyd's Cycle Detection (Tortoise and Hare)
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head: Optional[ListNode]) -> bool:
    """
    Detect cycle using Floyd's Tortoise and Hare algorithm.
    """
    if not head or not head.next:
        return False
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False


def has_cycle_hash_set(head: Optional[ListNode]) -> bool:
    """
    Detect cycle using a hash set (alternative approach).
    Time: O(n), Space: O(n)
    """
    seen = set()
    current = head
    
    while current:
        if current in seen:
            return True
        seen.add(current)
        current = current.next
    
    return False


# Test cases
if __name__ == "__main__":
    # Test case 1 - cycle present
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # Creates cycle
    assert has_cycle(node1) == True
    
    # Test case 2 - cycle to head
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2
    node2.next = node1  # Creates cycle
    assert has_cycle(node1) == True
    
    # Test case 3 - no cycle
    node1 = ListNode(1)
    assert has_cycle(node1) == False
    
    # Test case 4 - empty list
    assert has_cycle(None) == False
    
    print("All test cases passed!")
