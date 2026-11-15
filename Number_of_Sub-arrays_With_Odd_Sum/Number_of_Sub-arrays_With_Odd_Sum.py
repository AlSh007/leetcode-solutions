class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        res = odd = even = 0

        for num in arr:
            even += 1
            if num % 2:
                odd, even = even, odd
            res = (res + odd) % 1000000007
        
        return res