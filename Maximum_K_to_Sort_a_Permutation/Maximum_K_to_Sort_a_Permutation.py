class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        mask = (1 << 30) - 1

        for ind, val in enumerate(nums):
            if val != ind:
                mask &= val
        
        return 0 if mask == (1 << 30) - 1 else mask