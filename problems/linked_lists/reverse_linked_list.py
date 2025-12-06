"""
LeetCode 206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/

Given the head of a singly linked list, reverse the list, and return the 
reversed list.

Example 1:
    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]

Example 2:
    Input: head = [1,2]
    Output: [2,1]

Example 3:
    Input: head = []
    Output: []

Time Complexity: O(n)
Space Complexity: O(1) for iterative, O(n) for recursive
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list_iterative(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverse linked list iteratively.
    """
    prev = None
    current = head
    
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    return prev


def reverse_list_recursive(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverse linked list recursively.
    """
    if not head or not head.next:
        return head
    
    new_head = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    
    return new_head


# Helper functions for testing
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# Test cases
if __name__ == "__main__":
    # Test case 1
    head = create_linked_list([1, 2, 3, 4, 5])
    reversed_head = reverse_list_iterative(head)
    assert linked_list_to_list(reversed_head) == [5, 4, 3, 2, 1]
    
    # Test case 2
    head = create_linked_list([1, 2])
    reversed_head = reverse_list_iterative(head)
    assert linked_list_to_list(reversed_head) == [2, 1]
    
    # Test case 3 - empty list
    assert reverse_list_iterative(None) is None
    
    # Test recursive solution
    head = create_linked_list([1, 2, 3])
    reversed_head = reverse_list_recursive(head)
    assert linked_list_to_list(reversed_head) == [3, 2, 1]
    
    print("All test cases passed!")
