class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_num = max(nums)

        res = 0

        for num in nums:
            res += max_num - num
        
        return res