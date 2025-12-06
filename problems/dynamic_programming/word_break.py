"""
LeetCode 139. Word Break
https://leetcode.com/problems/word-break/

Given a string s and a dictionary of strings wordDict, return true if s can be 
segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the 
segmentation.

Example 1:
    Input: s = "leetcode", wordDict = ["leet","code"]
    Output: true
    Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
    Input: s = "applepenapple", wordDict = ["apple","pen"]
    Output: true
    Explanation: Return true because "applepenapple" can be segmented as 
                 "apple pen apple".

Example 3:
    Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
    Output: false

Time Complexity: O(n^2 * m) where n = len(s), m = average word length
Space Complexity: O(n)
"""

from typing import List


def word_break(s: str, word_dict: List[str]) -> bool:
    """
    Check if string can be segmented using DP.
    dp[i] = True if s[0:i] can be segmented
    """
    word_set = set(word_dict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True  # Empty string
    
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    
    return dp[n]


def word_break_optimized(s: str, word_dict: List[str]) -> bool:
    """
    Optimized DP using max word length.
    """
    word_set = set(word_dict)
    max_len = max(len(w) for w in word_dict) if word_dict else 0
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    
    for i in range(1, n + 1):
        # Only check words up to max_len
        for j in range(max(0, i - max_len), i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    
    return dp[n]


def word_break_bfs(s: str, word_dict: List[str]) -> bool:
    """
    BFS solution - treat as graph traversal.
    """
    from collections import deque
    
    word_set = set(word_dict)
    n = len(s)
    visited = set()
    queue = deque([0])
    
    while queue:
        start = queue.popleft()
        
        if start in visited:
            continue
        visited.add(start)
        
        for end in range(start + 1, n + 1):
            if s[start:end] in word_set:
                if end == n:
                    return True
                queue.append(end)
    
    return False


# Test cases
if __name__ == "__main__":
    # Test case 1
    assert word_break("leetcode", ["leet", "code"]) == True
    
    # Test case 2
    assert word_break("applepenapple", ["apple", "pen"]) == True
    
    # Test case 3
    assert word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False
    
    # Test case 4 - empty string
    assert word_break("", ["a"]) == True
    
    # Test optimized solution
    assert word_break_optimized("leetcode", ["leet", "code"]) == True
    
    # Test BFS solution
    assert word_break_bfs("leetcode", ["leet", "code"]) == True
    
    print("All test cases passed!")
