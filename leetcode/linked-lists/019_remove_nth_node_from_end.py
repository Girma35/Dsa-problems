"""
LeetCode Problem 19: Remove Nth Node From End of List
Difficulty: Medium
Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Problem:
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

Constraints:
- The number of nodes in the list is sz.
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Time Complexity: O(L) where L is the length of the list
        Space Complexity: O(1)
        
        Approach: Use two pointers with n gap between them.
        When fast reaches end, slow is at the node before the one to remove.
        """
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy
        
        # Move fast n+1 steps ahead
        for _ in range(n + 1):
            fast = fast.next
        
        # Move both pointers until fast reaches end
        while fast:
            slow = slow.next
            fast = fast.next
        
        # Remove the nth node
        slow.next = slow.next.next
        
        return dummy.next


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
    result = solution.removeNthFromEnd(head, 2)
    assert linkedlist_to_list(result) == [1, 2, 3, 5]
    
    # Test case 2
    head = list_to_linkedlist([1])
    result = solution.removeNthFromEnd(head, 1)
    assert linkedlist_to_list(result) == []
    
    # Test case 3
    head = list_to_linkedlist([1, 2])
    result = solution.removeNthFromEnd(head, 1)
    assert linkedlist_to_list(result) == [1]
    
    print("All test cases passed!")
