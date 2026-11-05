class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr1.sort()
        arr2.sort()
        ans = i = j = 0
        while i < len(arr1) and j < len(arr2): 
            if arr1[i] <= arr2[j] + d: 
                if arr1[i] < arr2[j] - d: ans += 1
                i += 1
            else: j += 1
        return ans + len(arr1) - i