class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()

        ans = []

        for ind, num in enumerate(nums):
            if num == target:
                ans.append(ind)
        
        return ans