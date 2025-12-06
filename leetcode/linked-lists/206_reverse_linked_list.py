"""
LeetCode Problem 206: Reverse Linked List
Difficulty: Easy
Link: https://leetcode.com/problems/reverse-linked-list/

Problem:
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:
- The number of nodes in the list is the range [0, 5000].
- -5000 <= Node.val <= 5000
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Approach: Iterative reversal using three pointers.
        """
        prev = None
        current = head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        return prev
    
    def reverseList_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Recursive approach.
        Time Complexity: O(n)
        Space Complexity: O(n) due to recursion stack
        """
        if not head or not head.next:
            return head
        
        new_head = self.reverseList_recursive(head.next)
        head.next.next = head
        head.next = None
        
        return new_head


# Helper functions for testing
def list_to_linkedlist(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linkedlist_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    head = list_to_linkedlist([1, 2, 3, 4, 5])
    result = solution.reverseList(head)
    assert linkedlist_to_list(result) == [5, 4, 3, 2, 1]
    
    # Test case 2
    head = list_to_linkedlist([1, 2])
    result = solution.reverseList(head)
    assert linkedlist_to_list(result) == [2, 1]
    
    # Test case 3
    head = list_to_linkedlist([])
    result = solution.reverseList(head)
    assert linkedlist_to_list(result) == []
    
    print("All test cases passed!")
