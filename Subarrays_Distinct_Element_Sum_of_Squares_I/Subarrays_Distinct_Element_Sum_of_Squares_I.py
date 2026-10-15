class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)

        ans = 0

        for l in range(n):
            seen, cnt = 0, 0
            for x in nums[l:]:
                cnt += ((seen >> x) & 1) == 0 #this checks if x is a distinct number not present on seen 
                seen |= (1 << x) 
                ans += cnt * cnt
        
        return ans