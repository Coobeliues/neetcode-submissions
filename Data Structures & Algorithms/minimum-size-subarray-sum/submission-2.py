import bisect
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        pref = [0] * (n + 1)
        res = float('inf')
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]
        
        for i in range(n):
            need = pref[i] + target
            j = bisect.bisect_left(pref, need)

            if j <= n:
                res = min(res, j - i)
        
        return 0 if res == float('inf') else res