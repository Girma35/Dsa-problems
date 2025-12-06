class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # stores number : index
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # If we already saw the complement, return answer
            if complement in seen:
                return [seen[complement], i]
            
            # Otherwise store this number's index
            seen[num] = i
