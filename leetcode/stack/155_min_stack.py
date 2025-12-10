"""
LeetCode Problem 155: Min Stack
Difficulty: Medium
Link: https://leetcode.com/problems/min-stack/

Problem:
Design a stack that supports push, pop, top, and retrieving the minimum element in 
constant time.

Implement the MinStack class:
- MinStack() initializes the stack object.
- void push(int val) pushes the element val onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.

Example 1:
Input:
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
Output: [null,null,null,null,-3,null,0,-2]

Constraints:
- -2^31 <= val <= 2^31 - 1
- Methods pop, top and getMin operations will always be called on non-empty stacks.
- At most 3 * 10^4 calls will be made to push, pop, top, and getMin.
"""


class MinStack:
    """
    Time Complexity: O(1) for all operations
    Space Complexity: O(n)
    
    Approach: Use two stacks - one for values, one for minimums.
    """
    
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Push to min_stack if it's empty or val is <= current min
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


class MinStackSingleStack:
    """
    Alternative: Store (val, current_min) pairs.
    """
    
    def __init__(self):
        self.stack = []  # Each element is (val, min_so_far)

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            current_min = min(val, self.stack[-1][1])
            self.stack.append((val, current_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Test cases
if __name__ == "__main__":
    # Test case 1
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    assert minStack.getMin() == -3
    minStack.pop()
    assert minStack.top() == 0
    assert minStack.getMin() == -2
    
    # Test case 2 with alternative implementation
    minStack2 = MinStackSingleStack()
    minStack2.push(-2)
    minStack2.push(0)
    minStack2.push(-3)
    assert minStack2.getMin() == -3
    minStack2.pop()
    assert minStack2.top() == 0
    assert minStack2.getMin() == -2
    
    print("All test cases passed!")
