"""
LeetCode Problem 141: Linked List Cycle
Difficulty: Easy
Link: https://leetcode.com/problems/linked-list-cycle/

Problem:
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached 
again by continuously following the next pointer.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node.

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Constraints:
- The number of the nodes in the list is in the range [0, 10^4].
- -10^5 <= Node.val <= 10^5
- pos is -1 or a valid index in the linked-list.
"""

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Approach: Floyd's Cycle Detection (Tortoise and Hare)
        Use two pointers, slow moves 1 step, fast moves 2 steps.
        If there's a cycle, they will meet.
        """
        if not head:
            return False
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        
        return False


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Cycle exists
    head = ListNode(3)
    node1 = ListNode(2)
    node2 = ListNode(0)
    node3 = ListNode(-4)
    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node1  # Creates cycle
    assert solution.hasCycle(head) == True
    
    # Test case 2: No cycle
    head = ListNode(1)
    head.next = ListNode(2)
    assert solution.hasCycle(head) == False
    
    # Test case 3: Single node, no cycle
    head = ListNode(1)
    assert solution.hasCycle(head) == False
    
    # Test case 4: Empty list
    assert solution.hasCycle(None) == False
    
    print("All test cases passed!")
