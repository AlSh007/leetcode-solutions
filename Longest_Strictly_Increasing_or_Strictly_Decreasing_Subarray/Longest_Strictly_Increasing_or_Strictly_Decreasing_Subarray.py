class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_len = inc = dec = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                inc += 1  # ↗️ Case
                dec = 1
            elif nums[i] < nums[i-1]:
                dec += 1  # ↘️ Case
                inc = 1
            else:
                inc = dec = 1  # \U0001f7e1 Case
            max_len = max(max_len, inc, dec)  # Update global max
        return max_len