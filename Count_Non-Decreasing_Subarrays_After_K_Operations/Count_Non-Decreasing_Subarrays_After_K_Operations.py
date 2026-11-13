class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        starts = deque()

        ans, water, right = 0, 0, len(nums) - 1
        for left in reversed(range(len(nums))):
            x = nums[left]

            while starts and nums[starts[0]] <= x:
                s = starts.popleft()
                end = starts[0] if starts else right + 1
                water += (x - nums[s]) * (end - s)

            starts.appendleft(left)
            while water > k:
                water -= nums[starts[-1]] - nums[right]
                if starts[-1] == right:
                    starts.pop()
                right -= 1
            ans += right -left + 1

        return ans 