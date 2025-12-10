"""
LeetCode 912. Sort an Array (Merge Sort)
https://leetcode.com/problems/sort-an-array/

Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(n log n) 
time complexity and with the smallest space complexity possible.

Example 1:
    Input: nums = [5,2,3,1]
    Output: [1,2,3,5]

Example 2:
    Input: nums = [5,1,1,2,0,0]
    Output: [0,0,1,1,2,5]

Merge Sort:
Time Complexity: O(n log n)
Space Complexity: O(n)
"""

from typing import List


def merge_sort(nums: List[int]) -> List[int]:
    """
    Sort array using merge sort.
    """
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    
    return merge(left, right)


def merge(left: List[int], right: List[int]) -> List[int]:
    """
    Merge two sorted arrays.
    """
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


def merge_sort_in_place(nums: List[int], left: int = 0, right: int = None) -> List[int]:
    """
    In-place merge sort (still O(n) space for merge step).
    """
    if right is None:
        right = len(nums) - 1
    
    if left < right:
        mid = (left + right) // 2
        merge_sort_in_place(nums, left, mid)
        merge_sort_in_place(nums, mid + 1, right)
        merge_in_place(nums, left, mid, right)
    
    return nums


def merge_in_place(nums: List[int], left: int, mid: int, right: int) -> None:
    """
    Merge two sorted subarrays.
    """
    left_arr = nums[left:mid + 1]
    right_arr = nums[mid + 1:right + 1]
    
    i = j = 0
    k = left
    
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            nums[k] = left_arr[i]
            i += 1
        else:
            nums[k] = right_arr[j]
            j += 1
        k += 1
    
    while i < len(left_arr):
        nums[k] = left_arr[i]
        i += 1
        k += 1
    
    while j < len(right_arr):
        nums[k] = right_arr[j]
        j += 1
        k += 1


# Test cases
if __name__ == "__main__":
    # Test case 1
    assert merge_sort([5, 2, 3, 1]) == [1, 2, 3, 5]
    
    # Test case 2
    assert merge_sort([5, 1, 1, 2, 0, 0]) == [0, 0, 1, 1, 2, 5]
    
    # Test case 3 - empty array
    assert merge_sort([]) == []
    
    # Test case 4 - single element
    assert merge_sort([5]) == [5]
    
    # Test in-place version
    nums = [5, 2, 3, 1]
    merge_sort_in_place(nums)
    assert nums == [1, 2, 3, 5]
    
    print("All test cases passed!")
