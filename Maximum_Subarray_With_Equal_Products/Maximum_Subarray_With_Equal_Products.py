from math import gcd, lcm

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 1

        for i in range(n):
            prod = g = l = nums[i]

            for j in range(i + 1, n):
                prod *= nums[j]
                g = gcd(g, nums[j])
                l = lcm(l, nums[j])

                if prod > g * l:
                    break
                if prod == g * l:
                    ans = max(ans, j - i + 1)

        return ans