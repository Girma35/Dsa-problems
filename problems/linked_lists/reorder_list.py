"""
LeetCode 143. Reorder List
https://leetcode.com/problems/reorder-list/

You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be 
changed.

Example 1:
    Input: head = [1,2,3,4]
    Output: [1,4,2,3]

Example 2:
    Input: head = [1,2,3,4,5]
    Output: [1,5,2,4,3]

Time Complexity: O(n)
Space Complexity: O(1)

Algorithm:
1. Find the middle of the list
2. Reverse the second half
3. Merge the two halves
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorder_list(head: Optional[ListNode]) -> None:
    """
    Reorder the list in place.
    """
    if not head or not head.next:
        return
    
    # Step 1: Find middle using slow and fast pointers
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    # Step 2: Reverse the second half
    second = slow.next
    slow.next = None  # Split the list
    prev = None
    while second:
        next_node = second.next
        second.next = prev
        prev = second
        second = next_node
    second = prev
    
    # Step 3: Merge the two halves
    first = head
    while second:
        tmp1 = first.next
        tmp2 = second.next
        first.next = second
        second.next = tmp1
        first = tmp1
        second = tmp2


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
    head = create_linked_list([1, 2, 3, 4])
    reorder_list(head)
    assert linked_list_to_list(head) == [1, 4, 2, 3]
    
    # Test case 2
    head = create_linked_list([1, 2, 3, 4, 5])
    reorder_list(head)
    assert linked_list_to_list(head) == [1, 5, 2, 4, 3]
    
    # Test case 3 - single node
    head = create_linked_list([1])
    reorder_list(head)
    assert linked_list_to_list(head) == [1]
    
    # Test case 4 - two nodes
    head = create_linked_list([1, 2])
    reorder_list(head)
    assert linked_list_to_list(head) == [1, 2]
    
    print("All test cases passed!")
