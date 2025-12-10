"""
LeetCode 155. Min Stack
https://leetcode.com/problems/min-stack/

Design a stack that supports push, pop, top, and retrieving the minimum element 
in constant time.

Implement the MinStack class:
- MinStack() initializes the stack object.
- void push(int val) pushes the element val onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.

Example 1:
    Input
    ["MinStack","push","push","push","getMin","pop","top","getMin"]
    [[],[-2],[0],[-3],[],[],[],[]]

    Output
    [null,null,null,null,-3,null,0,-2]

Time Complexity: O(1) for all operations
Space Complexity: O(n)
"""


class MinStack:
    """
    MinStack using two stacks - one for values, one for minimums.
    """
    
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, val: int) -> None:
        self.stack.append(val)
        # Push to min_stack if empty or val <= current min
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    
    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()
    
    def top(self) -> int:
        return self.stack[-1] if self.stack else None
    
    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else None


class MinStackSingleStack:
    """
    Alternative: Store (value, min_at_this_point) tuples.
    """
    
    def __init__(self):
        self.stack = []  # [(value, min_so_far)]
    
    def push(self, val: int) -> None:
        current_min = min(val, self.stack[-1][1]) if self.stack else val
        self.stack.append((val, current_min))
    
    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
    
    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None
    
    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else None


# Test cases
if __name__ == "__main__":
    # Test MinStack
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    assert min_stack.getMin() == -3
    min_stack.pop()
    assert min_stack.top() == 0
    assert min_stack.getMin() == -2
    
    # Test MinStackSingleStack
    min_stack = MinStackSingleStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    assert min_stack.getMin() == -3
    min_stack.pop()
    assert min_stack.top() == 0
    assert min_stack.getMin() == -2
    
    print("All test cases passed!")
