import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        mn = float('inf')
        while l <= r:
            m = l + (r - l) // 2
            k = 0
            for i in piles:
                k += math.ceil(i / m)
            if k <= h:
                mn = min(mn, m)
                r = m - 1
            else: l = m + 1
        return mn
