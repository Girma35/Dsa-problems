"""
LeetCode 19. Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Given the head of a linked list, remove the nth node from the end of the list 
and return its head.

Example 1:
    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]

Example 2:
    Input: head = [1], n = 1
    Output: []

Example 3:
    Input: head = [1,2], n = 1
    Output: [1]

Time Complexity: O(n)
Space Complexity: O(1)

Algorithm: Two Pointers (One Pass)
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    Remove nth node from end using two pointers with n gap.
    """
    dummy = ListNode(0, head)
    first = dummy
    second = dummy
    
    # Move first pointer n+1 steps ahead
    for _ in range(n + 1):
        first = first.next
    
    # Move both pointers until first reaches end
    while first:
        first = first.next
        second = second.next
    
    # Remove the nth node from end
    second.next = second.next.next
    
    return dummy.next


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
    result = remove_nth_from_end(head, 2)
    assert linked_list_to_list(result) == [1, 2, 3, 5]
    
    # Test case 2 - remove only node
    head = create_linked_list([1])
    result = remove_nth_from_end(head, 1)
    assert linked_list_to_list(result) == []
    
    # Test case 3 - remove last node
    head = create_linked_list([1, 2])
    result = remove_nth_from_end(head, 1)
    assert linked_list_to_list(result) == [1]
    
    # Test case 4 - remove first node
    head = create_linked_list([1, 2])
    result = remove_nth_from_end(head, 2)
    assert linked_list_to_list(result) == [2]
    
    print("All test cases passed!")
