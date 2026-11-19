import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        mx = r
        while l <= r:
            mid = l + (r - l) // 2
            s = 0
            for i in piles:
                s += math.ceil(i / mid)
            
            if s <= h:
                mx = mid
                r = mid - 1
            else: l = mid + 1

        return mx 