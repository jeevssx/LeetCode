class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashlol = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashlol:
                return [hashlol[diff], i]
            hashlol[n] = i