import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        mn = r

        while l <= r:
            m = l + (r - l) // 2
            total_t = 0
            for pile in piles:
                total_t += (pile + m - 1) // m
            
            if total_t <= h:
                mn = m
                r = m - 1
            else: l = m + 1
        
        return mn