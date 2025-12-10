"""
LeetCode 912. Sort an Array (Quick Sort)
https://leetcode.com/problems/sort-an-array/

Given an array of integers nums, sort the array in ascending order and return it.

Quick Sort:
Time Complexity: O(n log n) average, O(n^2) worst case
Space Complexity: O(log n) for recursion stack
"""

from typing import List
import random


def quick_sort(nums: List[int]) -> List[int]:
    """
    Sort array using quick sort.
    """
    if len(nums) <= 1:
        return nums
    
    def sort(arr, low, high):
        if low < high:
            pivot_idx = partition(arr, low, high)
            sort(arr, low, pivot_idx - 1)
            sort(arr, pivot_idx + 1, high)
    
    sort(nums, 0, len(nums) - 1)
    return nums


def partition(arr: List[int], low: int, high: int) -> int:
    """
    Partition array around pivot (Lomuto partition scheme).
    """
    # Use random pivot to avoid worst case
    pivot_idx = random.randint(low, high)
    arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]
    
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_simple(nums: List[int]) -> List[int]:
    """
    Simple quick sort (not in-place, easier to understand).
    """
    if len(nums) <= 1:
        return nums
    
    pivot = nums[len(nums) // 2]
    left = [x for x in nums if x < pivot]
    middle = [x for x in nums if x == pivot]
    right = [x for x in nums if x > pivot]
    
    return quick_sort_simple(left) + middle + quick_sort_simple(right)


def quick_sort_3way(nums: List[int]) -> List[int]:
    """
    Quick sort with 3-way partitioning (Dutch National Flag).
    Better for arrays with many duplicates.
    """
    def sort(arr, low, high):
        if low >= high:
            return
        
        # Random pivot
        pivot_idx = random.randint(low, high)
        arr[low], arr[pivot_idx] = arr[pivot_idx], arr[low]
        pivot = arr[low]
        
        # 3-way partition
        lt = low      # Elements < pivot go to [low, lt)
        gt = high     # Elements > pivot go to (gt, high]
        i = low + 1   # Current element
        
        while i <= gt:
            if arr[i] < pivot:
                arr[lt], arr[i] = arr[i], arr[lt]
                lt += 1
                i += 1
            elif arr[i] > pivot:
                arr[gt], arr[i] = arr[i], arr[gt]
                gt -= 1
            else:
                i += 1
        
        sort(arr, low, lt - 1)
        sort(arr, gt + 1, high)
    
    sort(nums, 0, len(nums) - 1)
    return nums


# Test cases
if __name__ == "__main__":
    # Test case 1
    assert quick_sort([5, 2, 3, 1]) == [1, 2, 3, 5]
    
    # Test case 2
    assert quick_sort([5, 1, 1, 2, 0, 0]) == [0, 0, 1, 1, 2, 5]
    
    # Test case 3 - empty array
    assert quick_sort([]) == []
    
    # Test case 4 - single element
    assert quick_sort([5]) == [5]
    
    # Test simple version
    assert quick_sort_simple([5, 2, 3, 1]) == [1, 2, 3, 5]
    
    # Test 3-way partition version
    assert quick_sort_3way([5, 2, 3, 1]) == [1, 2, 3, 5]
    
    print("All test cases passed!")
